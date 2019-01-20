'''
Python Program to Check if a Number is a Perfect Number

A perfect number is a whole number, an integer greater than zero; and

when you add up all of the factors less than that number, you get that number.

Examples:
The factors of 6 are 1, 2, 3 and 6.
1 + 2 + 3 = 6

The factors of 28 are 1, 2, 4, 7, 14 and 28.
1 + 2 + 4 + 7 + 14 = 28
'''

num = int(input("Enter the number: "))

total = 0

for  n in range(1, num):
    if (num % n == 0):
        total += n

if (total == num):
    print("Perfect Number")
else:
    print("Not Perfect Number")
