
# Modify a global scope

enemies = 2


def game():
    # global enemies
    # enemies += 1 
    return enemies+1

new_enemy = game()
print(new_enemy) 