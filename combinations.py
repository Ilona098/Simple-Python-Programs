# This is a Python Program to accept three distinct
# digits and print all possible combinations.
#

from itertools import permutations


numbers = []

max = 3

while len(numbers) < max:
    number = int(input(' Input number: '))
    numbers.append(number)

print('Your numbers are: ', numbers)

numebers2 = permutations(numbers)

print('Possible combinations: ')

count = 0
for i in list(numebers2):
    print(i)
    count +=1

print('There is ',count, 'combinations')