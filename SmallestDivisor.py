# The program takes in an integer and prints the smallest divisor of the integer.


number = int(input('Input a number:'))

list = []

for i in range(2,number+1):
    if (number%i==0):
        list.append(i)

list.sort()

print(list[0])

