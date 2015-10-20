
game_description = '''
        GAME DESCRIPTION:

        You wake up on the second floor of a tower
        building in a blaze of thick smoke. You attempt
        to gasp for air you desperately need. You soon
        find out that you had been knocked unconscious
        in the mist of a raging fire. You must escape
        to save your life. On your way out there will
        be essential items which are needed to aid
        your attempt to live. Only the correct items
        will lead you to the exit to save you from being
        engulfed by the fire. Otherwise you may die due
        to being smothered by the thick black smoke which
        is getting thicker and closer by the second.

        You are able to move left and right then up and
        down floors. There is a door located in the building
        which will allow you to escape. There is a fire exit
        towards the left hand side of the building. You are
        agonisingly close to the ground floor but not close
        enough to jump without dying. Also, on the roof is a
        helicopter, the helicopter has come to save you but
        you may find a few obstacles
        on the way.

<<<<<<< HEAD
        Finding the items throughout the building will help 
        you overcome the obstacles along the way. You can 
        only carry TWO ITEMS at a time. You can drop certain 
        items to pick up others, but you have to remember 
        where you left them. There is a chocolate bar that 
        you may pick up along your path, if your health is 
        below 50 it will give you 50 bonus points otherwise 
        if your above 50 then it regenerates your health back 
        to 100. You must think wisely to which exit will be 
        the easiest and quickest as your health will slowly 
        be decreasing due to the venomous fire and the 
        dangerous smoke. The more moves you take, the more 
        health you may lose, for example, moving from room 
        to room will differ from how many points it will 
=======
        Finding the items throughout the building will help
        you overcome the obstacles along the way. There is
        a chocolate bar that you may pick up along your path,
        if your health is below 50 it will give you 50 bonus
        points otherwise if your above 50 then it regenerates
        your health back to 100. You must think wisely to
        which exit will be the easiest and quickest as your
        health will slowly be decreasing due to the venomous
        fire and the dangerous smoke. The more moves you take,
        the more health you may lose, for example, moving from
        room to room will differ from how many points it will
>>>>>>> 326805f9f589e74fc4c513904aa4327c3866d0b0
        take from your health.

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

    start = input("Are you ready to start? >>> ")

    print("Starting game...")
