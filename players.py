# Find out who from the list has the most numbers matching lottery_numbers.

import random

# This line creates a set with 6 random numbers
lottery_numbers = set(random.sample(list(range(22)), 6))


players = [
    {'name': 'Ala', 'numbers': {1, 3, 5, 7, 9, 11}},
    {'name': 'Ilona', 'numbers': {2, 7, 9, 22, 10, 5}},
    {'name': 'Anna', 'numbers': {13, 14, 15, 16, 17, 18}},
    {'name': 'Adam', 'numbers': {19, 20, 12, 7, 3, 5}}
]

# Then, print out a line such as "Jen won 1000.".
# The winnings are calculated with the formula:
# 100 ** len(numbers_matched)



top_player = players[0]

for player in players:
    matched_numbers = len(player['numbers'].intersection(lottery_numbers))  # Calculate how many numbers they matched
    if matched_numbers > len(
            top_player['numbers'].intersection(lottery_numbers)):  # If they matched more than the current top player...
        top_player = player  # This player is the new top player

# Calculate their winnings using the formula.
winnings = 100 ** len(top_player['numbers'].intersection(lottery_numbers))


print('{} won {}.'.format(top_player['name'], winnings))
