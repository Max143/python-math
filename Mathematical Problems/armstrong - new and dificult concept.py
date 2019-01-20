'''
Python Program to Check if a Number is an Armstrong Number

num = 153

1*1*1 + 5*5*5 +3*3*3   = 153

153 == num <- Armstrong Number

'''
n=int(input("Enter any number: "))

string = str(n)

lst = list(string)

final = 0 

for i in lst:
  arms = pow(int(i),int(3))
  final += arms


if final == n:
  print("Armstrong Number")
else:
  print("Not Armstrong Number")

print("-------------------BooK Method-------------------------")

n=int(input("Enter any number: "))

a=list(map(int,str(n)))

b=list(map(lambda y:y**3,a))
if(sum(b)==n):
    print("The number is an armstrong number. ")
else:
    print("The number isn't an arsmtrong number. ")
























