# This is a Python Program to read a number n and print an identity matrix of the desired size.

n = int(input('Input a number: '))
list = []


if n>0:
    for j in range(0,n):

        for i in range(0,n):

            if (j == i):
                list.append(1)
            else:

                list.append(0)



new = [list[x:x+n]
for x in range(0,len(list),n)]

# Iterate through every sub-list in original list and unpack it in the print call with *
for matrix in new:
    print(*matrix)







