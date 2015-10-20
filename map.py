from items import *

roof_floor = {

    "name": "The Roof",

    "description": [

    """
    You have now entered the roof, on this floor
    there is a helicopter waiting to take you away
    from the blazing fire. In order to use the
    helicopter you will need a first aid kit, to
    aid the wounded pilot, and fuel.
    """,

    """
    You have now entered the roof, on this floor
    there is a helicopter waiting to take you away
    from the blazing fire. Unfortunately, in the time
    you have been gone the pilot has bled out. You are
    not able to fly the helicopter alone, find an
    alternative exit to escape the rising fire.

    You have already used the first aid kit to attempt
    to aid the pilot, it is now no use to your own health.
    The fuel you attained is now of no use.
    Your inventory has been cleared.
    """

    ],

    "exits": { "right": "Roof Stairwell" },

    "items": [item_key, item_rope],

    "damage": 0,

    "required_items": [item_fuel, item_first_aid]
}

roof_stairwell = {

    "name": "The Roof Stairwell",

    "description": [

    """
    You have now entered the top stairwell.
    From here you can go out onto the roof or
    go down to the second floor.
    """

    ],

    "exits": { "down": "Second Stairwell", "left": "Roof" },

    "items": [],

    "damage": 0,

    "required_items": []

}

third_floor = {
    "name": "The Third Floor",

    "description": [

    """
    You are now on the third floor. This is where the sprinkler control
    system for the building is located. Here you have the opportunity to
    increase your chance of survival by reducing the amount of damage you
    will receive from the smoke filled stairwells. You must break the
    glass to activate the sprinklers.


                    ----------------------------------
                   |  ------------------------------  |
                   |  |                            |  |
                   |  |                            |  |
                   |  |                            |  |
                   |  |        TAP TO BREAK        |  |
                   |  |            GLASS           |  |
                   |  |                            |  |
                   |  |                            |  |
                   |  |                            |  |
                   |  ------------------------------  |
                    ----------------------------------


    """

    ],

    "exits": { "left": "Third Fire Escape","right": "Third Stairwell" },

    "items": [],

    "damage": 0,

    "required_items": []
}

third_stairwell = {

    "name": "The Third Floor Stairwell",

    "description": [

    """
    You have now entered the third floor stairwell.
    From here you can go up to the roof or down to the
    second floor.
    """

    ],

    "exits": { "up": "Roof Stairwell", "down": "Second Stairwell", "left": "Third" },

    "items": [],

    "damage": 5,

    "required_items": []

}

third_fire_escape = {

    "name": "The Third Floor Fire Escape",

    "description": [

    """
    You step outside into the fresh air onto the
    fire escape, there is a ladder leading down to
    the second floor fire escape. You can go down to
    get the the second floor.
    """

    ],

    "exits": { "down": "Second Fire Escape", "right": "Third" },

    "items": [],

    "damage": 0,

    "required_items": []

}

second_floor = {

    "name": "The Second Floor",

    "description": [

    """
    You are on the second floor. The air is
    smokey and your vision is blurred. To your
    left you notice a door to a fire escape, and
    to your right you spot a smoke filled stairwell.
    Make a careful choice as to which route you
    take as this might affect your health.
    """

    ],

    "exits": { "left": "Second Fire Escape","right": "Second Stairwell" },

    "items": [item_first_aid],

    "damage": 0,

    "required_items": []

}

second_stairwell = {

    "name": "The Second Floor Stairwell",

    "description": [

    """
    You have now entered the second floor stairwell.
    From here you can go up to the third floor or down to the
    first floor.
    """

    ],

    "exits": { "up": "Third Stairwell", "down": "First Stairwell", "left": "Second" },

    "items": [],

    "damage": 5,

    "required_items": []

}

second_fire_escape = {

    "name": "The Second Floor Fire Escape",

    "description": [

    """
    You step outside into the fresh air onto the
    fire escape, there is a ladder leading down to
    the first floor fire escape. You can go down to
    get the the first floor or up to the third floor
    fire escape.
    """

    ],

    "exits": { "down": "First Fire Escape", "up": "Third Fire Escape", "right": "Second" },

    "items": [],

    "damage": 0,

    "required_items": []

}

first_floor = {

    "name": "The First Floor",

    "description": [

    """
    You are now on the first floor. The air is
    contaminated with thick smoke and you are finding
    it difficult to breathe. You can feel the heat
    rising from the stairwell which is to your right
    hand side. There is a fire exit to your left which
    appears to be safe.
    """

    ],

    "exits": { "left": "First Fire Escape", "right": "First Stairwell" },

    "items": [item_brick, item_fuel],

    "damage": 0,

    "required_items": []

}

first_stairwell = {

    "name": "The First Floor Stairwell",

    "description": [

    """
    You entered the first floor staircase, you can
    feel the fire roaring beneath you. You can not go
    down this staircase as it is engulfed with flames
    and smoke and would be incredibly dangerous.
    Please try another route.
    """

    ],

    "exits": { "up": "Second Stairwell", "left": "First" },

    "items": [],

    "damage": 10,

    "required_items": []

}

first_fire_escape = {

    "name": "The First Floor Fire Escape",

    "description": [

    """
    The fire escape to the ground floor is damaged,
    the ladder is not safe to use. You must collect
    a combination of suitable items to allow you to
    smash through the window to the ground floor as
    there is debris preventing you from dropping
    straight down.
    """,

    """
    You attach the hook and the rope to the fire
    escape. You have successfully attained the items
    which will allow you to cascade down to the ground
    floor. Your inventory has now been cleared.
    """

    ],

    "exits": { "up": "Second Fire Escape", "right": "First" },

    "items": [],

    "damage": 0,

    "required_items": [item_rope, item_brick]

}

ground_floor = {

    "name": "The Ground Floor",

    "description": [

    """
    The room is thick with smoke, you can barely see.
    You manage to stumble towards the front door and
    discover you do not have the items to open it.
    You explore the building carefully to gain the
    items that you require.
    """,

    """
    The room is thick with smoke, you can barely see.
    You manage to stumble towards the front door and
    use the items you gained to escape from the fire.
    Congratulations you have won your life.
    """

    ],

    "exits": { "up": "First Fire Escape", "right": "Ground Stairwell" },

    "items": [item_id],

    "damage": 0,

    "required_items": [item_key, item_id]

}

ground_stairwell = {

    "name": "The Ground Floor Stairwell",

    "description": [

    """
    You entered the ground floor staircase, it was
    filled with thick smoke and dangerous fire.
    You foolishly ran through the fire and burnt
    yourself badly, you have lost 50 of your health
    points.
    """

    ],

    "exits": { "up": "First Stairwell", "left": "Ground" },

    "items": [],

    "damage": 50,

    "required_items": []

}

rooms = {
    "Roof": roof_floor,
    "Roof Stairwell": roof_stairwell,
    "Third": third_floor,
    "Third Stairwell": third_stairwell,
    "Third Fire Escape": third_fire_escape,
    "Second": second_floor,
    "Second Stairwell": second_stairwell,
    "Second Fire Escape": second_fire_escape,
    "First": first_floor,
    "First Stairwell": first_stairwell,
    "First Fire Escape": first_fire_escape,
    "Ground": ground_floor,
    "Ground Stairwell": ground_stairwell
}
