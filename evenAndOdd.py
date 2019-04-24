# Python Program to Put Even and Odd elements in a List into Two Different Lists

num = int(input('How many numbers would you like to input: '))
list = []

for i in range(1, num+1):
    a = int(input("Input a number: "))
    list.append(a)

even = []
odd = []

for number in list:
    if (number%2==0):
        even.append(number)
    else:
        odd.append(number)

print("\nList of odd numbers: ", odd)
print("\nList of ven numbers: ", even)
