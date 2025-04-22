def is_prime(num):
    count=0
    if(num==1 and num ==0):
      print(f"{num} not a prime")
    else:
      for i in range (1,num+1):
         
         if(num%i==0):
           count+=1
    return count
    

a=is_prime(6)
if a==2:
   print("True")
else:
   print("False")
           
           
          
      
    