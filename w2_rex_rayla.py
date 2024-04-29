# Week 2: Meal Price Calculator
# Creativity: I added a tip option to the program. If the user chooses to leave a tip, they can input a percentage to tip. The tip amount is then calculated and added to the total. The user can then input the payment amount and the change is calculated.
# Author: Rex Rayla
# Git: https://github.com/KingSpearXX/Pathway
# Branch: week2

child_meal = float(input("What is the price of a child's meal? "))
adult_meal = float(input("What is the price of an adult's meal? "))
child_count = int(input("How many children are there? "))
adult_count = int(input("How many adults are there? "))

subtotal = (child_meal * child_count) + (adult_meal * adult_count)
print(f"\nSubtotal: ${subtotal:.2f}")

tax_rate = float(input("\nWhat is the sales tax rate? "))
tax = subtotal * (tax_rate / 100)
total = subtotal + tax
print(f"Sales Tax: ${tax:.2f}")
print(f"Total: ${total:.2f}")

tip_choice = input("\nWould you like to leave a tip? (y/n) ")
if tip_choice.lower() == "y":
    tip_rate = float(input("What percentage would you like to tip (0-100)? "))
    tip = total * (tip_rate / 100)
    total += tip
    print(f"Tip: ${tip:.2f}")
    print(f"Total with Tip: ${total:.2f}")

payment = float(input("\nWhat is the payment amount? "))
change = payment - total
print(f"Change: ${change:.2f}")

