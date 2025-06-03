# cook your dish here
count=0
i=0
str1=input()
while(i<len(str1)):
    if(str1[i]=='a' or str1[i]=='e' or str1[i]=='i' or str1[i]=='o' or str1[i]=='u'):
        count +=1
    i +=1
print(count)