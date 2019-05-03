# Python Program to Read a List of Words and Return the Length of the Longest One


list1 = []

element = int(input("Input number of elements in the list: "))

for i in range(1, element +1):
    a = input("Input a word: ")
    list1.append(a)


list1.sort(key=len, reverse=True)

longest = len(list1[0])

print("The longest word is: ", list1[0], " and have ", longest, " characters.")
