# Week 4: Word Game Puzzle
# Creativity: A random word is chosen from the list. There is a prompt to check if you are really close, added grades for the player.
# Author: Rex Rayla
# Git: https://github.com/KingSpearXX/Pathway
# Branch: week4

import random, os

class Grade:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

words = ["nephi","ether","kolob","mormon","moroni","jared","lehi","alma","helaman","samuel"]
grades = [
    Grade("Clairvoyant", 1), 
    Grade("Word Master", 3), 
    Grade("Pro Word Hunter", 5), 
    Grade("Rookie", 10), 
    Grade("Novice", 15)
    ]

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def mask_word(word):
    mask = "_ " * len(word)
    print (f"The word is: {mask}")

def word_game():
    while True:
        clear()
        print ("""
        Welcome to the Word Game Puzzle!
        
            Mechanics: [ctrl+c to exit] A word will be randomly selected from the list, you need to guess the word by typing the letters.
        A hint will be shown to you, if the letter is in the correct position, it will be displayed in uppercase.
        If the letter is in the word but not in the correct position, it will be displayed in lowercase.
        If the letter is not in the word, it will be displayed as _.""")
        input("\n\tPress any enter to continue...")
        
        word = random.choice(words)
        word_letters = list(word)
        word_length = len(word) 
        counter = 0

        while True: 
            clear()
            counter += 1
            mask_word(word)
            user_input = input(f"[ctrl+c to exit] Type a {word_length} letter word: ").lower()
            user_input_letters = list(user_input)
            if(len(user_input_letters) != word_length):
                print (f"\nYou must enter a {word_length} letter word! ")
                input ("\nPress any enter to continue...")
                continue
            if user_input == word:
                print (f"Congratulations! You have guessed the word! in {counter} tries.")
                
                for grade in grades:
                    if counter <= grade.grade:
                        print (f"\nYou have been graded as: {grade.name}")
                        break
                
                input ("\nPress any enter to continue...")
                break
            else:
                guess = ""
                for i in range(word_length):
                    if user_input_letters[i] == word_letters[i]:
                        guess += user_input_letters[i].upper() + " "
                    elif user_input_letters[i] in word_letters:
                        guess += user_input_letters[i].lower() + " "
                    else:
                        guess += "_ "
                if "_" not in guess:
                    print (f"\nYou are really close! Try again!")
                
                print (f"\nHint: {guess}")
                input ("\nPress any enter to continue...")
                
          
word_game()
