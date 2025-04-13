Student_scores=[210,150,40,170,50,80,89,30,200]
#I go by very long method 
# sorted=[]
# min=Student_scores[0]
# count=0
# for i in Student_scores:
#     if i>=min:
#         sorted.append(i)
#         count+=1


# print(sorted)
# print(len(sorted))
# a=(len(sorted))-1
# print(f"maximum Score is {sorted[a]}")


#shorter way
max=0
for i in Student_scores:
    if i>max:
        max=i
print(max)        