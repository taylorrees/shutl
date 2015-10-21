#!/usr/bin/python3

from map import rooms
from player import *
from items import *
from game_parser import *
from game_init import *
from random import randrange
from break_glass import *
import os
import time


def list_of_items(items):
    """This function takes a list of items (see items.py for the definition) and
    returns a comma-separated list of item names (as a string). For example:

    >>> list_of_items([item_key, item_rope])
    'a master key, some rope'

    >>> list_of_items([item_id])
    'an id card'

    >>> list_of_items([])
    ''

    >>> list_of_items([item_brick, item_chocolate, item_fuel])
    'a brick, a chocolate bar, some fuel'

    """

    s = ''
    for item in items:
        s = s + ', ' + item["name"]

    # remove the first ' ,'
    s = s[2:]

    return s


def print_room_items(room):
    """This function takes a room as an input and nicely displays a list of items
    found in this room (followed by a blank line). If there are no items in
    the room, nothing is printed. See map.py for the definition of a room, and
    items.py for the definition of an item. This function uses list_of_items()
    to produce a comma-separated list of item names. For example:

    >>> print_room_items(rooms["Roof"])
        There is a master key, some rope here.
    <BLANKLINE>

    >>> print_room_items(rooms["Second"])
        There is a first aid kit here.
    <BLANKLINE>

    >>> print_room_items(rooms["Ground Stairwell"])

    (no output)

    Note: <BLANKLINE> here means that doctest should expect a blank line.

    """

    items = list_of_items(room["items"])

    if items:
        s = "    There is %s here.\n" % items
        print(s)


def print_break():
    ''' This function prints a series of lines to the console. Two
    blank lines precede and succeed these lines in order to create
    some whitespace in the console.
    '''

    print("\n\n----------------------------------------------------------\n\n")


def print_inventory_items(items):
    """This function takes a list of inventory items and displays it nicely, in a
    manner similar to print_room_items(). The only difference is in formatting:
    print "You have ..." instead of "There is ... here.". For example:

    Also this function will display the total mass of the items that are currently
    in a players inventory.

    >>> print_inventory_items(inventory)

    """
    items = list_of_items(items)

    if items:
        s = "You have: %s.\n" % items
        print(s)


def find_in_inventory(inventory, item):
    '''Find a specific item by its id in the players inventory.
    Inventory must be passed as a list of dictionaries with each
    dictionary containing an id field. Item must be passed as a
    single dictionary containing an id field.
    '''

    for dictionary in inventory:
        if dictionary["id"] == item["id"]:
            return True
    return False


def clear_inventory():
    '''Removes all items in the players inventory.'''

    global inventory
    inventory = []


def find_required_items(inventory, required_items):
    '''This function takes a list of required item dictionaries and checks
    whether each item exists in the players inventory. If all the items are
    found the function will return True, otherwise it will return False.

    >>> find_required_items(inventory, "key")
    False
    '''

    # For each item in required items check if it exists in inventory.
    # If it doesn't set match to False

    match = True

    for item in required_items:
        result = find_in_inventory(inventory, item)
        if not result:
            match = False

    # If there are no required items there is no match.

    if not required_items:
        match = False

    return match

def room_description_selection(room):
    '''This function is responsible for printing the correct description
    depending on what items the player has in their inventory. If the items
    in their inventory do not match the required items for a room then it
    will print the default description (description[0]) otherwise the second
    description (description[1]) will be displayed. Also, if the items match
    the default description for the room is removed and replaced and the
    players inventory is cleared, as the items have been used to complete a
    task.
    '''

    required_items = room["required_items"]

    match = find_required_items(inventory, required_items)

    description = room["description"]

    # If there is a match show description[1] and remove the default
    # description from the list. Clear the players inventory.
    # Otherwise display the default description.

    if match:
        print(description[1])
        del description[0]
        clear_inventory()
    else:
        print(description[0])


def fix_fire_escape(room):
    '''This function will check if the room is the first floor fire escape.
    If it is and the required items are in the players inventory then the
    first floor fire escape will be repaired and the player can decend to the
    ground floor.
    '''

    if room["name"] == "The First Floor Fire Escape":
        if find_required_items(inventory, room["required_items"]):
            exit = {"down": "Ground"}
            room["exits"].update(exit)


def print_room(room):
    """This function takes a room as an input and nicely displays its name
    and description. The room argument is a dictionary with entries "name",
    "description" etc. (see map.py for the definition). The name of the room
    is printed in all capitals and framed by blank lines. Then follows the
    description of the room and a blank line again. If there are any items
    in the room, the list of items is printed next followed by a blank line
    (use print_room_items() for this). For example:

    >>> print_room(rooms["Roof"])
    <BLANKLINE>
    <BLANKLINE>
    ----------------------------------------------------------
    <BLANKLINE>
    <BLANKLINE>
        THE ROOF
    <BLANKLINE>
    <BLANKLINE>
    ----------------------------------------------------------
    <BLANKLINE>
    <BLANKLINE>
    <BLANKLINE>
        You have now entered the roof, on this floor
        there is a helicopter waiting to take you away
        from the blazing fire. In order to use the
        helicopter you will need a first aid kit, to
        aid the wounded pilot, and fuel.
    <BLANKLINE>
        There is a master key, some rope here.
    <BLANKLINE>
    <BLANKLINE>
    <BLANKLINE>
    ----------------------------------------------------------
    <BLANKLINE>
    <BLANKLINE>

    >>> print_room(rooms["Roof Stairwell"])
    <BLANKLINE>
    <BLANKLINE>
    ----------------------------------------------------------
    <BLANKLINE>
    <BLANKLINE>
        THE ROOF STAIRWELL
    <BLANKLINE>
    <BLANKLINE>
    ----------------------------------------------------------
    <BLANKLINE>
    <BLANKLINE>
    <BLANKLINE>
        You have now entered the top stairwell.
        From here you can go out onto the roof or
        go down to the second floor.
    <BLANKLINE>
    <BLANKLINE>
    <BLANKLINE>
    ----------------------------------------------------------
    <BLANKLINE>
    <BLANKLINE>

    >>> print_room(rooms["Second"])
    <BLANKLINE>
    <BLANKLINE>
    ----------------------------------------------------------
    <BLANKLINE>
    <BLANKLINE>
        THE SECOND FLOOR
    <BLANKLINE>
    <BLANKLINE>
    ----------------------------------------------------------
    <BLANKLINE>
    <BLANKLINE>
    <BLANKLINE>
        You are on the second floor. The air is
        smokey and your vision is blurred. To your
        left you notice a door to a fire escape, and
        to your right you spot a smoke filled stairwell.
        Make a careful choice as to which route you
        take as this might affect your health.
    <BLANKLINE>
        There is a first aid kit here.
    <BLANKLINE>
    <BLANKLINE>
    <BLANKLINE>
    ----------------------------------------------------------
    <BLANKLINE>
    <BLANKLINE>

    Note: <BLANKLINE> here means that doctest should expect a blank line.
    """
    # Display room name

    print_break()
    print("    " + room["name"].upper())
    print_break()

    fix_fire_escape(room)

    room_description_selection(room)

    print_room_items(room)
    print_break()


def exit_leads_to(exits, direction):
    """This function takes a dictionary of exits and a direction (a particular
    exit taken from this dictionary). It returns the name of the room into which
    this exit leads. For example:

    >>> exit_leads_to(rooms["Roof"]["exits"], "right")
    'The Roof Stairwell'
    >>> exit_leads_to(rooms["Roof Stairwell"]["exits"], "down")
    'The Second Floor Stairwell'
    >>> exit_leads_to(rooms["Second Fire Escape"]["exits"], "down")
    'The First Floor Fire Escape'
    """
    return rooms[exits[direction]]["name"]


def print_exit(direction, leads_to):
    """This function prints a line of a menu of exits. It takes a direction (the
    name of an exit) and the name of the room into which it leads (leads_to),
    and should print a menu line in the following format:

    GO <EXIT NAME UPPERCASE> to <where it leads>.

    For example:
    >>> print_exit("right", "The Roof Stairwell")
    Enter GO RIGHT to go to The Roof Stairwell.
    >>> print_exit("down", "The Second Floor Fire Escape")
    Enter GO DOWN to go to The Second Floor Fire Escape.
    """
    print("Enter GO " + direction.upper() + " to go to " + leads_to + ".")


def print_menu(exits, room_items, inv_items):
    """This function displays the menu of available actions to the player. The
    argument exits is a dictionary of exits as exemplified in map.py. The
    arguments room_items and inv_items are the items lying around in the room
    and carried by the player respectively. The menu should, for each exit,
    call the function print_exit() to print the information about each exit in
    the appropriate format. The room into which an exit leads is obtained
    using the function exit_leads_to(). Then, it should print a list of commands
    related to items: for each item in the room print

    "TAKE <ITEM ID> to take <item name>."

    and for each item in the inventory print

    "DROP <ITEM ID> to drop <item name>."

    For example, the menu of actions available at the Reception may look like this:

    You can:
    GO EAST to your personal tutor's office.
    GO WEST to the parking lot.
    GO SOUTH to MJ and Simon's room.
    TAKE BISCUITS to take a pack of biscuits.
    TAKE HANDBOOK to take a student handbook.
    DROP ID to drop your id card.
    DROP LAPTOP to drop your laptop.
    DROP MONEY to drop your money.
    What do you want to do?

    """
    print("You can:\n")
    # Iterate over available exits
    for direction in exits:
        # Print the exit name and where it leads to
        print_exit(direction, exit_leads_to(exits, direction))

    for item in room_items:
        # Print the item id and item name
        id = item["id"].upper()
        name = item["name"]
        print("Enter TAKE %s to take %s." % (id, name))

    for item in inv_items:
        # Print the item id and item name
        id = item["id"].upper()
        name = item["name"]
        print("Enter DROP %s to drop %s." % (id, name))

    print("Enter VIEW MAP to view a map.")

    print("\nWhat do you want to do?\n")


def is_valid_exit(exits, chosen_exit):
    """This function checks, given a dictionary "exits" (see map.py) and
    a players's choice "chosen_exit" whether the player has chosen a valid exit.
    It returns True if the exit is valid, and False otherwise. Assume that
    the name of the exit has been normalised by the function normalise_input().
    For example:

    >>> is_valid_exit(rooms["Ground Stairwell"]["exits"], "up")
    True
    >>> is_valid_exit(rooms["Ground Stairwell"]["exits"], "down")
    False
    >>> is_valid_exit(rooms["First Stairwell"]["exits"], "right")
    False
    >>> is_valid_exit(rooms["First Stairwell"]["exits"], "left")
    True
    """
    return chosen_exit in exits


def execute_go(direction):
    """This function, given the direction (e.g. "south") updates the current room
    to reflect the movement of the player if the direction is a valid exit
    (and prints the name of the room into which the player is
    moving). Otherwise, it prints "You cannot go there."
    """

    # Declare current_room as a global variable (avoids unbound local error)
    global current_room
    # Get the exits for the current room
    exits = current_room["exits"]

    if is_valid_exit(exits, direction):
        current_room = move(exits, direction)
        print(">>> You're moving into %s." % current_room["name"])
    else:
        print(">>> You cannot go there.")


def inventory_mass():
    """ This function calculates the total mass of all the items currently
    stored in the players inventory. This can be used to calculate whether
    another item can be added to the inventory.
    """

    total_mass = 0

    for item in inventory:
        total_mass += item["mass"]

    return total_mass


def eat_choc():
    """This function is responsible for adding to health
    when a chocolate bar is taken. If the health is 50 hp
    or above then health is reset. Otherwise 50 hp will be added.
    """

    global health

    if health >= 50:
        health = 100
    else:
        health += 50

    current_room["items"].remove(item_chocolate)



def execute_take(item_id):
    """This function takes an item_id as an argument and moves this item from the
    list of items in the current room to the player's inventory. However, if
    there is no such item in the room, this function prints
    "You cannot take that."
    """

    if item_id == "chocolate":
        eat_choc()
    else:

        items = current_room["items"]


        # Set default result of match for item to False
        match = False

        for item in items:
            if item["id"] == item_id:
                # If the item is found set match to True
                match = True
                break

        # If the match condition is True add item to
        # inventory and remove from the current room

        if match and len(inventory) < 2:
            inventory.append(item)
            items.remove(item)
            print(">>> You took %s." % item["name"])
        else:
            print(">>> You cannot take that. (Hint: You cannot carry more than two items at a time.)")




def execute_drop(item_id):
    """This function takes an item_id as an argument and moves this item from the
    player's inventory to list of items in the current room. However, if there is
    no such item in the inventory, this function prints "You cannot drop that."
    """

    items = current_room["items"]

    match = False
    for item in inventory:
        if item["id"] == item_id:
            match = True
            break

    if match:
        items.append(item)
        inventory.remove(item)
        print("You dropped %s." % item["name"])
    else:
        print(">>> You cannot drop that.")


def execute_view(item):
    """This function is responsible for printing the game map
    into the console for the player to view.

    >>> execute_view("map")
    <BLANKLINE>
            GAME MAP:
    <BLANKLINE>
                    _                                 _
                    |       ROOF          Stairwell   |
                    |____________________ _______   _ |
            Fire    |                    |        _   |
            Escape  |                    |      _     |
                    |       THIRD        |    _       |
                                            _         |
            |==|___________________________    _______|
            |==|    |                    |  _         |
            |==|    |                    |    _       |
            |==|    |       SECOND       |      _     |
            |==|                                  _   |
            |==|___________________________    _______|
            |==|    |                    |  _         |
            |==|    |                    |    _       |
            |==|    |       FIRST        |      _     |
            |==|                                  _   |
            |==|______________________________________|
                    |                    |        _   |
                    |                    |            |
                            GROUND       |   Fire     |
            Debris  |                    |  _         |
            ........|____________________|____________|
    <BLANKLINE>
    <BLANKLINE>
            START:
    >>> execute_view("go right")

    """

    if item == "map":
        print(visual_map)
        start = input("Press enter to continue game >>> ")
        print("Continuing game...")


def execute_command(command):
    """This function takes a command (a list of words as returned by
    normalise_input) and, depending on the type of action (the first word of
    the command: "go", "take", or "drop"), executes either execute_go,
    execute_take, or execute_drop, supplying the second word as the argument.

    >>> execute_command(["go"])
    <BLANKLINE>
    >> Go where?
    >>> execute_command(["take"])
    <BLANKLINE>
    >> Take what?
    >>> execute_command(["move"])
    <BLANKLINE>
    >> This makes no sense.
    """

    print()

    if 0 == len(command):
        return

    if command[0] == "go":
        if len(command) > 1:
            execute_go(command[1])
        else:
            print("Go where?")

    elif command[0] == "take":
        if len(command) > 1:
            execute_take(command[1])
        else:
            print("Take what?")

    elif command[0] == "drop":
        if len(command) > 1:
            execute_drop(command[1])
        else:
            print("Drop what?")

    elif command[0] == "view":
        if len(command) > 1:
            execute_view(command[1])
        else:
            print(">> View what?")

    else:
        print(">> This makes no sense.")



def menu(exits, room_items, inv_items):
    """This function, given a dictionary of possible exits from a room, and a list
    of items found in the room and carried by the player, prints the menu of
    actions using print_menu() function. It then prompts the player to type an
    action. The players's input is normalised using the normalise_input()
    function before being returned.
    """

    # Display menu
    print_menu(exits, room_items, inv_items)

    # Read player's input
    user_input = input(">>> ")

    # Normalise the input
    normalised_user_input = normalise_input(user_input)


    if normalised_user_input == ["use", "lift"]:
        return True

    return normalised_user_input


def move(exits, direction):
    """This function returns the room into which the player will move if, from a
    dictionary "exits" of avaiable exits, they choose to move towards the exit
    with the name given by "direction". For example:

    >>> move(rooms["First"]["exits"], "left") == rooms["First Fire Escape"]
    True
    >>> move(rooms["First Stairwell"]["exits"], "up") == rooms["Second Stairwell"]
    True
    >>> move(rooms["First Stairwell"]["exits"], "up") == rooms["Second"]
    False
    """

    # Next room to go to
    return rooms[exits[direction]]


def has_won():
    """ This function determines whether or not the user has won the game.
    It defines the victory criteria. The victory criteria are that all items
    in the game must be dropped at reception.
    """

    if current_room == rooms["Ground"]:
        required_items = current_room["required_items"]
        items_found = find_required_items(inventory, required_items)
        if items_found:
            return True



def health_is(health, room):
    """ This function is responsible for calculating the players health
    from their existing health and the damage attained from the room they
    are in. Accepts health as an integer value and room as a dictionary
    with a field damage.
    >>> health_is(health, rooms["Roof"])
    100
    >>> health_is(65, rooms["Second Stairwell"])
    55
    >>> health_is(0, rooms["Second Stairwell"])
    -10
    """

    damage = (room["damage"])
    return (health - damage)


def random_place_choc(rooms):
    """This function is responsible for the random placement of the item item_chocolate.
    It loops through each of the rooms apart from the ground floor and the ground floor
    stairwell and selects a room at random in which to place the item.
    """

    potential_rooms = [
        "Roof",
        "Roof Stairwell",
        "Third",
        "Third Stairwell",
        "Third Fire Escape",
        "Second",
        "Second Stairwell",
        "Second Fire Escape",
        "First",
        "First Stairwell",
        "First Fire Escape"
    ]

    stop = len(potential_rooms)
    n = randrange(0, stop)
    room = rooms[potential_rooms[n]]
    room["items"].append(item_chocolate)

def clear_screen():
    """This function detects the OS and runs the clear screen
    code for that OS. Also pauses the screen before clearing
    so that messages can be read.
    """

    # Pause execution
    time.sleep(0.5)

    # Clear the game screen
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')



# This is the entry point of our program
def main():

    # Provides the user with a description and visual map
    # at the start of the game. Located in game_init.py

    try:
        game_init()
        random_place_choc(rooms)

        # Main game loop
        while True:

            global health

            clear_screen()

            # check whether the player has met the victory criteria
            if has_won():

                print("\nCONGRATULATIONS YOU WON!")
                print("\nBut you really Should Have Used The Lift (SHUTL).\n")
                break

            else:

                try:

                    # Display game status (room description, inventory etc.)
                    print_room(current_room)
                    print_inventory_items(inventory)

                    health = health_is(health, current_room)
                    print ("Your health is: " + str(health))
                    print

                    if health <= 0:
                        print ("YOU ARE DEAD SUCKER")
                        break

                    if current_room == rooms["Third"]:
                        break_glass_game()

                    # Show the menu with possible actions and ask the player
                    command = menu(current_room["exits"], current_room["items"], inventory)

                    if command == True:
                        print("\nCONGRATULATIONS SMART PERSON, YOU WON!\n")
                        break

                    # Execute the player's command
                    execute_command(command)

                except KeyboardInterrupt:

                    quit = input("\nAre you sure you want to quit? (Y/N) >>> ")
                    if quit.upper().strip() == "Y":
                        break
                    else:
                        print("Resuming game...")
                        pass

                except EOFError:
                    print("You cannot do that.")
                    pass

    # Allows the user to quit the game gracefully.
    except KeyboardInterrupt:
        print("You quit the game.")
        pass


# Are we being run as a script? If so, run main().
# '__main__' is the name of the scope in which top-level code executes.
# See https://docs.python.org/3.4/library/__main__.html for explanation
if __name__ == "__main__":
    main()
