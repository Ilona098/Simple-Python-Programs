# This is a Python Program to read a number n and print the natural numbers summation pattern.
#
n = int(input('Input a number: '))

count = 0
list = []

while (count<n):
    count +=1
    list.append(count)

    pat = ' + '.join(map(str,list))

    print(sum(list),'=',pat)






