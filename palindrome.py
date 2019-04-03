# The program takes a number, word or sentence and checks whether it is a palindrome or not.


a = input('Input a number, word or sentence:')


list = []

for i in a:
    list.append(i)

list.reverse()
rev = "".join(list)

if a == rev:
    print(rev, ' Is a palindrome ', a)
else:
    print(rev, ' Is not a palindrome ', a)

