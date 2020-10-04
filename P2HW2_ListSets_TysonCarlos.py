# CTI-110
# P2HW2 - List and Sets
# Carlos Tyson
# 9/24/2020
#

a = input('Enter a value: ')
b = input('Enter a value: ')
c = input('Enter a value: ')
d = input('Enter a value: ')
e = input('Enter a value: ')
f = input('Enter a value: ')
g = input('Enter a value: ')
h = input('Enter a value: ')
i = input('Enter a value: ')
j = input('Enter a value: ')

numbers = [a, b, c, d, e, f, g, h, i, j]

print("The lowest number in the list is:" , min(numbers))
print("The highest number in the list is:" , max(numbers))
print("Sum of numbers in the list is:", sum(numbers))

avg = sum(numbers)/len(numbers)
print("The average of list is:", avg)

setlist1 = set(numbers)
print(setlist1)
