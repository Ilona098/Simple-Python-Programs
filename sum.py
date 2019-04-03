# This is a Python Program to find the sum of digits in a number.


number = input("Input a number: ")

sum = 0

for digit in number:
    sum = sum + int(digit)

print(sum)