n=int(input("Number of students"))
record=[]
for _ in range(n):
    name=input("name:")
    mark=float(input("mark:"))
    record.append([name,mark])
print(record)    

sort_record=sorted(record,key=lambda x:x[1])
print(sort_record)
# second_low=sort_record[1][1]
# print(len(sort_record))
low=sort_record[1][1]
second_low=[]
for x in sort_record:
    if(x[1]==low):
        second_low.append(x[0])

sort_secondLow=sorted(second_low)
for i in sort_secondLow:
    print(i)   