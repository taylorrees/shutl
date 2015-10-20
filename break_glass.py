
import time
from map import rooms


victory_string = '''

    By doing this you have removed some of the smoke from the air.
    Thus removing the damage you would have experienced by walking
    in the stairwells.

    CONGRATULATIONS
    '''

failure_string = '''
    You did not manage to smash the glass.
    '''

def count_hits(seconds):
    """This function is responsible for counting the number of `hits`
    the user inputs. A hit is determined by the input of a blank string.
    This function will run for a specified amount of seconds. The
    seconds must be passed in as an integer.
    """

    print("""
    You have %s seconds in which to break the glass, good luck!
    """ % seconds)

    count = 0
    end = time.time() + seconds

    while time.time() < end:
        usr = input()
        if usr == '':
            count += 1

    return count


def has_won(hits, required_hits):
    """This function takes seconds as an integer and required_hits
    as an integer and determines whether the player managed to break
    the glass. Seconds is required to call count_hits.
    """

    if hits >= required_hits:
        return True

    return False


def remove_damage(rooms):
    """This function loops through all the rooms and sets their damage
    values to zero. The rooms dictionary must be passed into the function.
    """

    for room in rooms:
        rooms[room]["damage"] = 0
    rooms["Ground Stairwell"]["damage"] = 50


def break_glass_game():

    seconds_to_run = 5
    required_hits = 40

    while True:

        print("""
        To break the glass you must repeatedly hit the return key on your
        keyboard.
        """)
        # Ask the user if they wish to play.
        play = input("Do you wish to play? (Y/N) >>> ")

        # If they want to play.
        if play.upper().strip() == "Y":

            # Count the number of hits.
            hits = count_hits(seconds_to_run)
            won = has_won(hits, required_hits)

            print('>>> %s hits' % hits)

            if won:
                remove_damage(rooms)
                print('YOU SMASHED THE GLASS')
                print(victory_string)
            else:
                print(failure_string)

            time.sleep(1)
            break

        # If they do not.
        elif play.upper().strip() == "N":

            print("\nYou have chosen not to play.\n")
            break

        # If the input is not understood.
        else:

            print("\nI'm sorry, I didn't understand that.\n")
