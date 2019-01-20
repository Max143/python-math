# Program to check whether the entered number is prime or not

num = int(input("Enter the number : "))

if num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            print(num, "is not a prime number ")
            print(i, "times", num//i, "is ", num)
            break
    else:
        print(num, "is a prime number")
else:
    print(num, "is not a prime number")


print("GeeksOfGeek Method")

def isPrime(n) : 
  
    # Corner cases 
    if (n <= 1) : 
        return False
    if (n <= 3) : 
        return True
  
    # This is checked so that we can skip  
    # middle five numbers in below loop 
    if (n % 2 == 0 or n % 3 == 0) : 
        return False
  
    i = 25
    while(i * i <= n) : 
        if (n % i == 0 or n % (i + 2) == 0) : 
            return False
        i = i + 6
  
    return True
  
  
# Driver Program  
if (isPrime(11)) : 
    print(" true") 
else : 
    print(" false") 
      
if(isPrime(15)) : 
    print(" true") 
else :  
    print(" false") 


#  modified program - Find the prime number in given range

# Not Solved yet  
lower = int(input("Enter the lower range: "))
upper = int(input("Enter the upper range: "))

Not_prime = []
prime = []
five = []


    
def main():
    for i in range(lower, upper+1):
        if i > 1 :
                if (i % 2 == 0 or i % 3 == 0 ):
                    Not_prime.append(i)
                else:
                    prime.append(i)
        else:   
            Not_prime.append(i)


for i in range(lower, upper+1):
    if (i % 5 == 0):
        
    elif ( i % 5 == 0):
        five.append(i)
    

print("These number are not prime: ",Not_prime)
print("------------------------------------")
print("These number are prime: ",prime)
            






















