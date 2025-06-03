# a=input()
# b=a.split()
# s=""
# for i in b:
#     if(i.isnumeric()):
#         s +=i+" "
#     else:
#         s +=i.capitalize()+" "

# print(dir(a))
# if(a.isnumeric):
#     print(a)
# else:
#     print(a.title())
# print(s)
def solve(s):
    b = s.split()
    t = ""
    for i in b:
        if i.isnumeric():
            t += i + " "
        else:
            t += i[0].upper() + i[1:] + " "
    return t.strip()  # To remove the extra space at the end

s=input()
print(solve(s))