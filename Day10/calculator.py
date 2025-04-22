import art

# This code logic is my this code are perform in easy way by angela mam
print(art.logo)
def add(n1,n2):
    return n1+n2

def subtract(n1,n2):
    return n1-n2

def division(n1,n2):
    return n1/n2

def multiply(n1,n2):
    return n1*n2


operations={
    "+":add,
    "-":subtract,
    "/":division,
    "*":multiply
}
#print(operations["*"](4,8)) #here n1=4 n2=8
n1=int(input("Enter a number1 : "))
for symbol in operations:
    print(symbol)
operator=input("Choose operator: ")
n2=int(input("Enter a number2: "))
answer=operations[operator](n1,n2)
print(answer)
should_continue=True
while should_continue:
    choice=input("If you off to calculator then say: 'off' \n If you want to continue with same answer say 'yes' otherwise 'no':  ")
    if(choice=="off"):
      should_continue=False 
    elif(choice=="yes"):
   
        for symbol in operations:
          print(symbol)
        operator=input("Choose operator: ")
        n2=int(input("Enter a number2 :"))
        if(operator=="+"):
            answer=operations[operator](answer,n2)
            print(answer)
        elif(operator=="-"):
            answer=operations[operator](answer,n2)
            print(answer)
        elif(operator=="*"):
            answer=operations[operator](answer,n2)
            print(answer)
        elif(operator=="/"):
            answer=operations[operator](answer,n2)
            print(answer)
 
    else:     
        n1=int(input("Enter a number1 :"))
        for symbol in operations:
          print(symbol)
        operator=input("Choose operator: ")
        n2=int(input("Enter a number2 :"))
        if(operator=="+"):
            print(operations[operator](n1,n2))
        elif(operator=="-"):
            print(operations[operator](n1,n2))
        elif(operator=="*"):
            print(operations[operator](n1,n2))
        elif(operator=="/"):
            print(operations[operator](n1,n2))
