"""
Program Name: Deal Cards
Author: Nana Gyampoh
Purpose: This program simulates dealing a hand of cards based on user input.
Date: February 8, 2026
"""

import random

# List of card values and suits
values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
suits = ["c", "h", "s", "d"]

# Ask user how many cards they want
num_cards = int(input("How many cards would you like? "))

hand = []  # list to store dealt cards

# Deal cards without repeats
while len(hand) < num_cards:
    value = random.choice(values)
    suit = random.choice(suits)
    card = value + suit

    if card not in hand:
        hand.append(card)

# Display the hand
print("Your hand:")
print(hand)

# Print total number of cards
print("Total cards dealt:", num_cards)