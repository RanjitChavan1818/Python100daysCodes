# A={1,3}
# B={5}
# arr=[]
# for _ in range(4):
#    a=list(map(int,input().split()))
#    arr.append(a)
# print(arr) 
# score=0
# brr=[]
# for x in arr:
#    for i in x:
#       if i not in brr:
#          brr.append(i)
# print(brr)   

# for i in brr:
#    if i in A:
#       score +=1
#    elif i in B:
#       score -=1
# print(score)      
         


# B={5,7}
# a=[1,5,3]
# score=0
# for i in a:
#     if i in A:
#         score +=1
#     elif i in B:
#         score -=1
# print(score)
# print(f"{m} {n}")






n, m = map(int, input().split())
S = list(map(int, input().split()))  
A = list(map(int, input().split()))  
B = list(map(int, input().split()))  

new_A = set(A)
new_B = set(B)
score = 0
for i in S:
    if i in new_A:
        score += 1
    if i in new_B:
        score -= 1
print(score)

    