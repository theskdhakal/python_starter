
alphabet=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'] 


direction=input("Type 'encode ' to encrypt, type 'decode ' to decrypt: \n")
text=input("Type your message: \n").lower()
shift=input("Type the shift number: \n")

def encrypt(text,shift):
    
    encrypted_message=''
  
    for letter in text:
        i=alphabet.index(letter)
        new_i=i+int(shift)
        encrypted_message += alphabet[new_i]
    
    print(encrypted_message)
    

if direction=='encode':
    encrypt(text,shift)

# print(encrypted_message)
      