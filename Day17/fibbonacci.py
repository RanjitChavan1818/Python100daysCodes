a=0
b=1
arr=[0,1]
n=15

j=1
while(j<=n-2):
    c=a+b
    a=b
    b=c
    arr.append(c)
    j+=1
print(arr)    