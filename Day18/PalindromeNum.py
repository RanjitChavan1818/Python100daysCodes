# n=121
# temp=n
# sum=0
# while(temp>0):
#     sum=sum*10+temp%10
#     temp=temp//10

# if(n==sum):
#     print("true")
# else:
#     print("false")
class Solution(object):
    def isPalindrome(self, x):
      temp=x
      num=0
      while(temp>0):
        num=num*10+temp%10
        temp=temp//10
      if num==x:
        return "true"
      else:
         return "false"   


s=Solution()
a=int(input())
print(s.isPalindrome(a)  )
