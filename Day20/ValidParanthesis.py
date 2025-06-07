s="[(])"
stack=[]
for i in s:
  if (i=="(" or i=="{" or i=="["):
    stack.append(i)
print(stack)    

for i in s:
  if (i==")"):
    stack.remove("(")
  if (i=="]"):
    stack.remove("[")
  if (i=="}"):
    stack.remove("{")

if(len(stack)==0):
  print("valid")
else:
  print("Not valid")
  