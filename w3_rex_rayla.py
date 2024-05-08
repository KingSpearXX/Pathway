# Week 3: Adventure Game
# Creativity: Added a secret choice "fly", I created a function to present the choice and use a loop to make sure to get the correct response. No more nested if since choices are stored in a variable.
# Author: Rex Rayla
# Git: https://github.com/KingSpearXX/Pathway
# Branch: week3

def choice(context, choice1, choice2):
    while True:
        print(context)
        user_input = input(f"What do you choose? {choice1.upper()}/{choice2.upper()}:").lower()
        if user_input == choice1:
            return 1
        elif user_input == choice2:
            return 2
        elif user_input == "fly":
            print("You fly away from the game. *!@#$% there's a glitch in the Matrix!!!.")
            exit()
        else:
            print("Invalid choice. Please try again.")

# Door choice
print("Welcome to the Adventure Game!")
print("You are standing in a room with two doors.")
door = choice("Which door do you want to enter?", "left", "right")
if door == 1:
    print("You enter the left door and find a chest full of gold.")
else:
    print("You enter the right door and find a chest of a sword and shield.")

# Merchant choice
print("You exit the room and find yourself in a forest.")
print("You see a merchant selling potions.")
buy = choice("Do you want to buy a potion?", "yes", "no")
if buy == 1 and door == 1:
    print("You buy a potion and drink it. You feel a surge of energy and gain 10 health.")
elif buy == 1 and door == 2:
    print("You have no gold to buy a potion. You leave the merchant and continue on your journey.")
else:
    print("You leave the merchant and continue on your journey.")

# Dragon choice and key
key = 0
alive = 1
print("You continue through the forest and see a dragon.")
print("The dragon is sleeping.")
attack = choice("Do you want to attack the dragon?", "yes", "no")
if attack == 1 and door == 1:
    print("You attack the dragon and it wakes up. You are burned to a crisp.")
elif attack == 1 and door == 2:
    print("You attack the dragon and it wakes up. You fight valiantly and defeat the dragon. You find a key to a door in the dragon's lair.")
    key = 1
else:
    print("You leave the dragon alone and continue through the forest.")

if attack == 1 and door == 1 and buy == 1:
    print("You used the potion to heal yourself and continue on your journey. The dragon was impressed by your bravery and gives you a key to a door in the dragon's lair!")
    key = 1
elif attack == 1 and door == 1 and buy == 2:
    print("You did not have a potion to heal yourself.")
    alive = 0

# Final choice
if key == 1 and alive == 1:
    print("You find the door the key unlocks and enter.")
    print("You find a room with a chest full of treasure.")
    print("Congratulations! You have completed the Adventure Game!")

if key == 0 and alive == 1:
    print("You did not find the key to the door. You are lost in the forest. Game Over.")

if alive == 0:
    print("You have perished in the game. Game Over.")





