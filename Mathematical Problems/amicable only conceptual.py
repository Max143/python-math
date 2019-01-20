'''
Amicable Number:

pari of number (220, 284)

Factors sum of 220 is 284 and
Factors sum 284 is 220.
'''


a = int(input("Enter a: "))
b = int(input("Enter b: "))

a_lst = []
a_sum = 0   
for i in range(1, a):
    if a % i == 0:
        a_sum += i
        a_lst.append(i)
        
b_lst = []
b_sum = 0
for i in range(1, b):
    if b % i == 0:
        b_sum += i
        b_lst.append(i)


if a_sum == b and b_sum == a:
    print("Amicable")
else:
    print("Not amicable")
    

