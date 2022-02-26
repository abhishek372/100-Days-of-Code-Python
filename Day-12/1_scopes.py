############ Scope ############

enemies = 1

def increase_enemies():
    enemies = 2
    print(f"Enemies inside function: {enemies}")

increase_enemies()
print(f"Enemies outside function: {enemies}.")


############ Local Scope ############
def increase_potion():
    potion_strength = 20
    print(potion_strength)

increase_potion()
print(potion_strength)        # Throws error as potion_strength is defined only inside function


############ Global Scope ############
player_health = 10      # Global variable

def drink_potion():
    potion_strength = 2
    print(potion_strength)
    print(player_health)    

drink_potion()


# Scopes are not only for variables, it also applies for function

############ Block Scope ############
# There is no block scopes in python 

enemies = ['Skeleton', 'Zombies', 'Alien']
game_level = 3

# Inside the blocks like if, else, while, for 
# variables are not block level they can be used outside of that

def game():
    if game_level<5:
        new_enemy = enemies[0]

# Throws error
print(new_enemy)        # Now, new_enemy become local variable for game() function


