# enemies = 1

# def increase_enemies():
#     enemies = 2
#     print(f"enemies inside function: {enemies}")

# increase_enemies()
# print(f"enemies outside function: {enemies}")


# #Local Scope
# def drink_potions():
#     potion_strength = 2
#     print(potion_strength)

# drink_potions()

#Global Scope
# player_health = 10

# def game():
#     def drink_potions():
#         potion_strength = 2
#         print(player_health)
    
#     drink_potions()
    
# print(player_health)

# #There is no Block Scope

# game_level = 3
# enemies = ["Skeleton", "Zombie", "Alien"]
# if game_level < 5:
#     new_enemy = enemies[0]

# print(new_enemy)

# #Modifying Global Scope
# enemies = 1

# def increase_enemies():
#     print(f"enemies inside function: {enemies}")
#     return enemies + 1

# enemies = increase_enemies()
# print(f"enemies increased function: {enemies}")

#Global Constants

PI = 3.14159

def calc():
    return PI

print(calc())