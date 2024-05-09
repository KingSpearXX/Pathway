# Week 3: Adventure Game
# Creativity: Added a secret choice "fly", I created a function to present the choice and use a loop to make sure to get the correct response. No more nested if since choices are stored in a variable.
# Author: Rex Rayla
# Git: https://github.com/KingSpearXX/Pathway
# Branch: week3
import os, time

items = []

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def choice(context, choices):
    while True:
        print(context)
        print ("\nChoices: ")
        choice_str = "[EXIT] [ITEMS] "
        for choice in choices:
            choice_str += f"[{choice.upper()}] "
        print(f"{choice_str}")
        user_input = input(f"\nWhat do you choose?: ").lower()
        if user_input in choices:
            return user_input
        elif user_input == "exit":
            clear()
            print("Goodbye!")
            exit()
        elif user_input == "items":
            clear()
            print("\nItems: ")
            for item in items:
                print(f"{item.upper()}")
            input("\nPress any key to continue...")
            clear()
        else:
            print("Invalid choice, try again! \n")
            time.sleep(0.5)
            clear()

def message(msg):
    print(f"\n{msg}\n")


                 
# Start of the game
clear()
terrain = choice ("You are in a forest, you see a path to the mountain and a path to the river, where do you want to go?", ["mountain", "river"])

# Terrain
while True:
    clear()

    # Items in the terrain
    if terrain == "mountain" and "potion" not in items:
        message("You found a potion, along the way!")
        items.append("potion")
    if terrain == "river" and "sword" not in items:
        message("You found a sword, along the way!")
        items.append("sword")

    if terrain == "mountain":
        direction = choice("You are now in the mountain, You see two paths, one to the north, one to the right that leads to the river.", ["north", "right"])
    if terrain == "river":
        direction = choice("You are now in the river, You see two paths, one to the north, one to the left that leads to the mountain.", ["north", "left"])
    if direction == "north":
        break
    elif direction == "left":
        terrain = "mountain"
    elif direction == "right":
        terrain = "river"

# Event
event_action = ""
while True:
    clear()
    if terrain == "mountain":
        event_action = choice("You see an old man stuck in a broken carriage, What would you like to do?", ["help", "ignore", "potion"])

    if event_action == "help":
        clear()
        message("You helped the old man, but he still died from his wounds. You proceed to the north.")
        event_action = "north"
        break
    elif event_action == "potion" and "potion" in items:
        clear()
        message("You helped and used the potion to heal the old man, in return he gave you a key. You proceed to the west.")
        items.remove("potion")
        items.append("key")
        event_action = "west"
        break
    elif event_action == "potion" and "potion" not in items:
        clear()
        message("You don't have any potion to use!")
        input("\nPress any key to continue...")
    elif event_action == "ignore":
        clear()
        message("You ignored the old man and headed east.")
        terrain = "river" 
        input("\nPress any key to continue...")
        clear()
    
    if terrain == "river":
        event_action = choice("You see a barbarian king, What would you like to do?", ["fight", "run", "surrender"])
    
    if event_action == "run":
        clear()
        message("You ran away from the barbarian king, you proceed to the west.")
        terrain = "mountain"
        input("\nPress any key to continue...")
    elif event_action == "surrender":
        clear()
        message("You surrendered to the barbarian king, he took all your items and you proceed to the east.")
        items.clear()
        terrain = "mountain"
        input("\nPress any key to continue...")
        clear()
    elif event_action == "fight" and "sword" in items:
        clear()
        message("You fought the barbarian king and won, you proceed to the west.")
        event_action = "east"
        break
    elif event_action == "fight" and "sword" not in items:
        clear()
        message("You fought the barbarian king and lost, you proceed to the north.")
        event_action = "north"
        break

# Ending
if terrain == "mountain" and event_action == "north":
    message("You found a new city, you settled down. Game Over!")
if terrain == "mountain" and event_action == "west" and "key" not in items:
    message("You found a golden gate but could not unlock it you continued your journey. Game Over!")
if terrain == "mountain" and event_action == "west" and "key" in items:
    message("You found a golden gate and used the key to open it, you became the lord of the manor. Game Over!")
if terrain == "river" and event_action == "east":
    message("You became the barbarian king after defeating the previous leader. Game Over!")
if terrain == "river" and event_action == "north" and "potion" not in items:
    message("You suffered severe injury and died. Game Over!")
if terrain == "river" and event_action == "north" and "potion" in items:
    message("You suffered severe injury, but with the help of the potion you survived and continued your journey. Game Over!")