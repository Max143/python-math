'''
Python Program to Check if a Number is a Strong Number
'''
import math
num = int(input("Enter the number: "))

string = str(num)
lst = []

for i in string:
  lst.append(i)


# print(lst)  # for debugging purpose

match = 0

for number in lst:
  total = math.factorial(int(number))
  # print(total)  # For debugging purpose
  match += total
  
# print(match)  # check the su of all factorial of digit of given num

# checking whether the match == num or not:
if match == num:
  print("It is a strong number.")
else:
  print("It is not a strong number.")




print(" Another Difficult Method by Sandfoundry")


sum1=0

num=int(input("Enter a number:"))

temp=num

while(num):
    i=1
    f=1
    r=num%10
    while(i<=r):
        f=f*i
        i=i+1
    sum1=sum1+f
    num=num//10
if(sum1==temp):
    print("The number is a strong number")
else:
    print("The number is not a strong number")



total = 0

num = int(input("Enter the number: "))

temp = num

while(num):
  i = 1
  digit_total_value = 1
  digit = num % 10
  while(i <= digit):
    digit_total_value *=  1
    i += 1
  total += digit_total_value # add the final value  of digit_total_value when we get to total 
  # that first iterating will get a last digit of 145 is 5 and while loop will find the 1 factorial until specified condition in the parameter of while that more than 1 and up tp 5, then finally we get the digit_total_value == 120. Then at this step add into the total bucket
  num = num // 10

if (total == temp):
  print("strong number")
else:
  print("Not Strong Number")

