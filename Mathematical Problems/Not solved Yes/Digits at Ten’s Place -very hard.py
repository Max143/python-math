'''
Python Program to Form an Integer that has the Number of Digits at Ten’s Place and the Least Significant Digit of the Entered Integer at One’s Place


sanfoundary source
'''


n=int(input("Enter the number:"))
tmp=n
k=0
while(n>0):
    k=k+1
    n=n//10
b=str(tmp)
c=str(k)
d=c+b[k-1]
print("The new number formed:",int(d))
