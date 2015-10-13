
roof_floor = {
    "name": "The Roof",
    "description": "",
    "exits": { "right": "Roof Stairwell" },
    "items": []
}

roof_stairwell = {
    "name": "The Roof Stairwell",
    "description": "",
    "exits": { "down": "Second Stairwell", "left": "Roof" },
    "items": []
}

second_floor = {
    "name": "The Second Floor",
    "description": "",
    "exits": { "left": "Second Fire Escape","right": "Second Stairwell" },
    "items": []
}

second_stairwell = {
    "name": "The Second Floor Stairwell",
    "description": "",
    "exits": { "up": "Roof Stairwell", "down": "First Stairwell", "left": "Second" },
    "items": []
}

second_fire_escape = {
    "name": "The Second Floor Fire Escape",
    "description": "",
    "exits": { "down": "First Fire Escape", "right": "Second" },
    "items": []
}

first_floor = {
    "name": "The First Floor",
    "description": "",
    "exits": { "left": "First Fire Escape", "right": "First Stairwell" },
    "items": []
}

first_stairwell = {
    "name": "The First Floor Stairwell",
    "description": "",
    "exits": { "up": "Second Stairwell", "left": "First" },
    "items": []
}

first_fire_escape = {
    "name": "The First Floor Fire Escape",
    "description": "",
    "exits": { "up": "Second Fire Escape", "right": "First" },
    "items": []
}

ground_floor = {
    "name": "The Ground Floor",
    "description": "",
    "exits": { "right": "Ground Stairwell" },
    "items": []
}

ground_stairwell = {
    "name": "The Ground Floor Stairwell",
    "description": "",
    "exits": { "up": "First Stairwell", "left": "Ground" },
    "items": []
}

rooms = {
    "Roof": roof_floor,
    "Roof Stairwell": roof_stairwell,
    "Second": second_floor,
    "Second Stairwell": second_stairwell,
    "Second Fire Escape": second_fire_escape,
    "First": first_floor,
    "First Stairwell": first_stairwell,
    "First Fire Escape": first_fire_escape,
    "Ground": ground_floor,
    "Ground Stairwell": ground_stairwell
}
