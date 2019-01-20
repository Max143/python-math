'''
Python Program to Find Those Numbers which are Divisible by 7 and Multiple of 5 in a Given Range of Numbers
'''

for i in range(int(input("Enter the lower range: ")),int(input("Enter the upper range: "))):
  if (i % 7 == 0) and (i % 5 == 0):
    print(i, end=',')


print("--------------")
print("Using List comprehension method")

lst = [i for i in range(int(input("Lower range: ")), int(input("Upper range: "))) if i % 7 == 0 and i % 5 == 0]

print(lst)

