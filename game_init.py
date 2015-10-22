
game_description = '''
        GAME DESCRIPTION:

        You wake up on the second floor of a tower
        building in a blaze of thick smoke. You are gasping
        for the air you so desperately need. You soon
        discover out that you had been knocked unconscious
        in the mist of a raging fire. You must escape
        to save your life.

        On your way out there will be some
        essential items which are needed to aid
        your attempt to live. Only the correct items
        will lead you to the exit to save you from being
        engulfed by the fire. As the black smoke gets
        thicker and closer by the second there is a
        risk that you will be smothered. You are able to
        move left, right, up and down between floors.

        There is a door located in the building
        which will allow you to escape. There is a fire exit
        towards the left hand side of the building. This will
        take you agonisingly close to the ground floor,
        but not close enough to jump, without dying. Also,
        on the roof is a helicopter. The helicopter has come
        to save you, but you may discover a few obstacles
        along the way.

        Finding the items throughout the building will help
        you overcome these obstacles. You can only carry TWO
        ITEMS at a time. You can drop certain items to pick
        up others, but you have to remember where you left them.

        There is a chocolate bar that will be randomly placed
        within the game. If you manage to find the choclate
        on your travels, you may pick it up. If your health is
        below 50 HP, it will add 50 health points, otherwise
        it will regenerate your health back to 100.

        You must think wisely to which exit will be
        the easiest and quickest to use as your health will slowly
        be decreasing due to the venomous fire and the
        dangerous smoke. The more moves you take, the more
        health you may lose. Moving from room to room will
        differ how many health points you will lose.

        Choose your moves wisely.
'''

visual_map = '''
        GAME MAP:

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



        '''


def game_init():
    '''This functions will print the game description and visual
    map (both above) to the console.
    '''

    print(game_description)
    print(visual_map)
    print("SCROLL UP TO VIEW GAME DESCRIPTION\n")

    start = input("Press enter to start >>> ")

    print("Starting game...")
