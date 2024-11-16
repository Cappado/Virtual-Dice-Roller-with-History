# dice_roller_with_history.py

import random

history = []

def roll_dice():
    roll = random.randint(1, 6)
    history.append(roll)
    return roll

# Sample usage
print("Rolled:", roll_dice())
print("History:", history)
