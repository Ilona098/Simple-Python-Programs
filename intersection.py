# This is a Python Program to find the intersection of two lists.

def intersection(list1, list2):
    return list(set(list1) & set(list2))

ele1 = int(input("Input a number of elements in first list: "))


list1 = []
list2 = []


for i in range(1, ele1+1):
    a = input("Input a number: ")
    list1.append(a)

ele2 = int(input("Input a number of elements in second list: "))

for j in range(1, ele2+1):
    b = input("Imput a number: ")
    list2.append(b)


print("The intersection is: ", intersection(list1, list2))