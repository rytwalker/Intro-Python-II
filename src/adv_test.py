from room import Room
from player import Player
from item import Item

# Declare all the rooms
room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}

items = {
    'key': Item('Key', 'It\'s a key to something'),
    'sword': Item('Sword', 'It\'s a weapon'),
    'mouse': Item('Mouse', 'It could be a pet'),
    'map': Item('Map', 'Helps you get around'),
    'backpack': Item('Backpack', 'Holds more items'),
    'yo-yo': Item('Yo-Yo', 'A fun toy'),
    'water': Item('Water', 'Stay hydrated'),
}


# Link rooms together
room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

# Place items in rooms
room['foyer'].items = [items['key'].name, items['sword'].name]
room['overlook'].items = [items['mouse'].name, items['yo-yo'].name]
room['narrow'].items = [items['backpack'].name]
room['treasure'].items = [items['water'].name]

#
# Main
#


def try_direction(direction, current_room):
    attribute = direction + '_to'
    # see if inputted direction is one we can move to
    if hasattr(current_room, attribute):
        # fetch the new room
        return getattr(current_room, attribute)
    else:
        print('You can\'t go that way. Try a different direction.')
        return current_room

# Make a new player object that is currently in the 'outside' room.


# Init a new player to play the game
# set current room to outside
player = Player(room['outside'])

# game loop
while True:
    # Display current room and desc
    print(player.current_room)
    # Display items in room
    if len(player.current_room.items):
        print(f"There are some items here: {player.current_room.items}")
    else:
        print('There are no items in this room')
    # User enters a command
    user_input = input('> ').lower().split(' ')

    # If Item command
    if len(user_input) == 2:
        if user_input[0] == 'get' or user_input[0] == 'take':
            item_count = len(player.current_room.items)
            for i, item in enumerate(player.current_room.items):
                if item.lower() == user_input[1]:
                    player.items.append(player.current_room.items.pop(i))
                    print(f"Updated inventory: {player.items}")
        elif user_input[0] == 'drop':
            item_count = len(player.items)
            for i, item in enumerate(player.items):
                if item.lower() == user_input[1]:
                    player.current_room.items.append(player.items.pop(i))
                    print(f"Updated inventory: {player.items}")
    elif len(user_input) == 1:
        if user_input[0] == 'q':
            print('You left the game, game over!')
            break
        if user_input[0] == 'i' or user_input[0] == 'inventory':
            print(f"inventory: {player.items}")

        player.current_room = try_direction(user_input[0], player.current_room)
