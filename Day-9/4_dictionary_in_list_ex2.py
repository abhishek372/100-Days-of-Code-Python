# Program that adds new items to travel_log

travel_log = [
    {
        "state":" Gujarat",  
        "visits": 12,
        "cities": ['Baroda', 'Surat', 'Rajkot', 'Ahmedabad']
    },
    {
        "state": "Maharashtra", 
        "visits": 8,
        "cities": ['Mumbai', 'Pune', 'Nashik', 'Nagpur']
    },
]

# Function to add new item to the travel_log list
def add_new_state(state_visited, times_visited, cities_visited):
    new_state = {}
    new_state["state"] = state_visited
    new_state["visits"] = times_visited
    new_state["cities"] = cities_visited
    travel_log.append(new_state)

# Calling the function
add_new_state("Uttar Pradesh", 15, ['Ayodhya', 'Noida', 'Lucknow', 'Kanpur'])

print(travel_log)



