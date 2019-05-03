# Python Program to Sort a List According to the Length of the Elements

list1 = []

ele = int(input("Input number of elements in the list: "))

for i in range(1, ele +1):
    a = input("Input an element: ")
    list1.append(a)


list1.sort(key=len)

print("List sorted by the length: ",list1)
