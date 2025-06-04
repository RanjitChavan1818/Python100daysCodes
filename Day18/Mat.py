def design(n,m):
    for _ in range(n):
        print("-",end="")
    for _ in range(m):    
        print(".|.",end="")   
    for _ in range(n):
        print("-",end="") 
    print() 

def center(b):
    c=(b-7)//2
    for _ in range(c):
        print("-",end="")
    print("WELCOME",end="")
    for _ in range(c):
        print("-",end="")
    print()    
    

a,b=map(int,input("Enter numbers:").split())      
N=a//2 
n=1

m=3*N
while(m>=3 ):
    design(m,n)
    n +=2
    m -=3
center(b)  

m1=3
n1=a-2   
while(m1<=3*N):
    design(m1,n1)
    m1 +=3
    n1 -=2
