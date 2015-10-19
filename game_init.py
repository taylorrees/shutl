
game_description = '''
        GAME DESCRIPTION:

        You wake up on the second floor of the Queens
        building of Cardiff University in a blaze of
        thick smoke as you attempt to gasp for air you
        desperately need. You soon find out that you
        had been knocked unconscious in the mist of a
        raging fire. You must escape to save your life.
        On your way out there will be essential items
        which are needed to aid your attempt to live,
        only the correct item will aid the correct exit
        and save you from being engulfed by the fire or
        dying due to being smothered by the thick black
        smoke which is getting thicker and closer by
        the second.

        You are able to move left and right then up a
        floor or down a floor. There is a door to get out
        on the bottom floor which will allow you to escape
        and breathe the air you badly need, a fire exit
        towards the left hand side of the building, although
        you are agonisingly close to the ground floor but
        not close enough to jump without dying. Also, on the
        roof is a helicopter, the helicopter has come to save
        you but you may find a few obstacles on the way.

        Gaining the items along the way will help you no
        end, you must think wisely to which exit will be
        the easiest and quickest as your health will slowly
        be cascading due to the venomous fire and the dangerous
        smoke. The more moves you take, the more health you
        will lose, for example, a health draining climb up
        the steep steps of stairs will steal 5 health points.
        Chose your moves wisely.
'''

visual_map = '''
        GAME MAP:

                _                                 _
                |       ROOF          Stairwell   |
                |____________________ _______   _ |
        Fire    |                    |        _   |
        Escape  |                    |      _     |
                |       SECOND       |    _       |
                                        _         |
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


        START:'''


def game_init():
    '''This functions will print the game description and visual
    map (both above) to the console.
    '''

    print(game_description)
    #print(visual_map)
