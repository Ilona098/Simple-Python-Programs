# This is a Python Program to merge two lists and sort it.
import collections

list1 = []
list2 = []

numbers1 = int(input("Input number of elements in first list: "))

for i in range(1, numbers1+1):
    a = int(input("Input a number: "))
    list1.append(a)

numbers2 = int(input("Input number of elements in second list: "))

for i in range(1, numbers2 + 1):
    b = int(input("Input a number: "))
    list1.append(b)

list3 = list1 + list2

list3.sort()

print("Sorted list is: ", list3,'\n')


counter = collections.Counter(list3)

no_duplicates = list(set(counter))

common = counter.most_common()


print("The list without repetitions is: ", no_duplicates,'\n')
print("The most common element is ", common[0][0],"and occurrence ", common[0][1]," times.")