# a=input("Enter space-separated values: ")
# string_list=a.split()
# print(string_list)
# b=tuple(string_list)
# print(hash(b))
# b=map(tuple,int.split(""))
# print(dir(b))
# print(hash(b))
n = int(input())

Tuple1 = map(int, input().split())

t = tuple(Tuple1)

print(hash(t))