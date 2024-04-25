# Week 1: Mad Libs Activity
# Author: Rex Rayla
# Git: https://github.com/KingSpearXX/Pathway
# Branch: week1

import random


def determine_article(word):
    if word[0].lower() in 'aeiou':
        return 'an'
    return f'a {word}'

def pluralize_noun(noun):
    if noun.endswith('y') and noun[-2] not in 'aeiou':
        return noun[:-1] + 'ies'
    elif noun.endswith(('s', 'ss', 'sh', 'ch', 'x', 'z')):
        return noun + 'es' 
    elif noun.endswith('f'):
        return noun[:-1] + 'ves'
    elif noun.endswith('fe'):
        return noun[:-2] + 'ves'
    else:
        return noun + 's'

def verb_to_ed(verb):
    if verb.endswith('ed'):
        return 'had to ' + verb
    return 'had to ' + verb + ' to'

def verb_to_ing(verb):
    if verb.endswith('e') and verb != "be":
        return verb[:-1] + 'ing'
    elif len(verb) > 1 and verb[-1] not in 'aeiou' and verb[-2] in 'aeiou' and verb[-3] not in 'aeiou':
        return verb + verb[-1] + 'ing'
    else:
        return verb + 'ing'

def create_story():
    print("Please Enter the following:\n")

    adjectives = []
    verbs = []

    kid = input("Enter a kid's name: ")
    adjectives.append(input("Enter an adjective: "))
    adjectives.append(input("Enter another adjective: "))
    adjectives.append(input("and another adjective: "))
    animal = input("Enter an animal: ")
    noun = input("Enter a noun: ")
    verbs.append(input("Enter a verb: "))
    verbs.append(input("Enter another verb: "))
    verbs.append(input("and another verb: "))
    food = input("Enter a type of food: ")
    emotion = input("Enter an emotion: ")
    
    story = f"""
        Once upon a time, there was {determine_article(random.choice(adjectives))} kid
    named {kid.title()}. One day, {kid.title()} decided to visit the {random.choice(adjectives)} zoo.
    At the zoo, the first thing {kid.title()} saw was {determine_article(random.choice(adjectives))} {animal} 
    eating {pluralize_noun(noun.title())}. It was very {random.choice(adjectives)} to see that!
    
        Next, {kid.title()} saw {determine_article(random.choice(adjectives))} {animal} that
    was {verb_to_ing(random.choice(verbs))} with a {noun.title()}. {kid.title()} laughed and said, 
    "That's the most {determine_article(random.choice(adjectives))} thing I've ever seen!"

        Later, {kid.title()} got to feed {determine_article(random.choice(adjectives))} {animal}. 
    It gently took the {food} from (his/her) 
    hand and {verb_to_ed(random.choice(verbs))} it up in one bite!

        But the most {determine_article(random.choice(adjectives))} part of the day was when
    {determine_article(random.choice(adjectives))} {animal} escaped from its enclosure.
    Everyone {verb_to_ed(random.choice(verbs))} in surprise as zookeepers
    chased it around. In the end, they used {determine_article(noun.title())} to
    coax it back into its home.

        Finally, tired but {emotion}, {kid.title()} went home,
    already excited about the next {random.choice(adjectives)} adventure
    at the zoo.
    """

    # Print the story
    print("\nHere's your story:")
    print(story)

create_story()
