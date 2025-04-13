alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']




def caesar(text,shift,encode_or_decode):
    cipher_text=""

    for letter in text:
        
        if letter not in alphabet: #This condition check which letter not in alpahbet, which keep as it is
            cipher_text+=letter
        else:
            if encode_or_decode=="decode": #By keeping this condition inside for loop it changes shift by + and - . It flipfloping
                shift*=-1
            shift_position=alphabet.index(letter)+shift
            shift_position%=len(alphabet)
            cipher_text+=alphabet[shift_position]

    
    print(f"Here is the {encode_or_decode}d result {cipher_text}")


should_continue=True
while should_continue :
    direction=input("Type encrypt for encode, Type decrypt decode : ").lower()
    text=input("type a message : ").lower()
    shift=int(input("ENter number to be shift : "))

    caesar(text,shift,direction)
    check=input("You want to continue say 'yes', for stop say 'no'").lower()
    if check=="no":
        should_continue=False
      
