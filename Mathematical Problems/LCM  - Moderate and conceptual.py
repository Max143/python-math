# Try using recrsive functions
lst = [2,4,6,8,10,12]  # LCM 120
print(lst)
#count = 0 count < len(lst)
while(1):
    for n in lst:
      n1 = n
      lst.remove(n)
      n2 = lst[0]
      lst.remove(n2)
      #print(n1,n2)
      #count += 1
      new  = []
      if (n1>n2):
        num = n1
      else:
        num = n2
        while(1):
          if (num % n1 == 0 and num % n2 == 0):
            print("LCM: ", num)
            new.append(num) # to store lcm value of iterating
            print(new)
            num += 1
      
      
'''
new  = []
if (n1>n2):
  num = n1
else:
  num = n2
  while(1):
    if (num % n1 == 0 and num % n2 == 0):
      print("LCM: ", num)
      new.append(num) # to store lcm value of iterating
      print(new)
      num += 1


'''
      
'''
def main(n1,n2):
      new  = []
      if (n1>n2):
        num = n1
      else:
        num = n2
        while(1):
          if (num % n1 == 0 and num % n2 == 0):
            print("LCM: ", num)
            new.append(num) # to store lcm value of iterating
            print(new)
            num += 1
    
          



def next():
  while(1):
    for n in lst:
      n1 = n
      lst.remove(n)
      n2 = lst[0]
      lst.remove(n2)

      #print(n1,n2)
      main(n1,n2)
    
next()
    
'''

        

        




