# Nesting list in a dictionary
travel_log = {
    "Gujarat": ['Ahmedabad', 'Baroda', 'Surat', 'Rajkot'],
    "Madhya Pradesh": ['Bhopal', 'Indore', 'Gwalior', 'Jabalpur']
}

# Nesting dictionary in a dictionary
travelled_cities = {
    "Guajarat": {"cities_visited": ['Baroda', 'Surat', 'Rajkot'], "total_visits": 12},
    "Maharashtra": {"cities_visited":['Mumbai', 'Pune', 'Nashik'], "total_visits": 8},
}

# Nesting dictionary in a list
travelled_cities = [
    {
        "state":" Gujarat", 
        "cities_visited": ['Baroda', 'Surat', 'Rajkot'], 
        "total_visits": 12
    },
    {
        "state": "Maharashtra", 
        "cities_visited": ['Mumbai', 'Pune', 'Nashik'], 
        "total_visits": 8
    },
]

