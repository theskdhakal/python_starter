
from art import logo

print(logo)

alphabet=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',] 




# def encrypt(text,shift):
   
  
#     encrypted_message=''
#     for letter in text:
#         i=alphabet.index(letter)
#         new_i=i+int(shift)
#         encrypted_message += alphabet[new_i]
    
#     print(f'the encoded text is {encrypted_message}')


# def decrypt(text,shift):

#     decrypted_message=''

#     for letter in text:
#         i=alphabet.index(letter)
#         original_i=i - int(shift)
#         decrypted_message -= alphabet[original_i]
    
#     print(f"the original messsage is {decrypted_message}")


# if direction=='encode':
#     encrypt(text,shift)
    
# elif direction=='decode':
   
#      decrypt(text,shift)


def ceaser(direction,text,shift):
    message=""

    if direction=='decode':
            shift *= -1

    if shift >26:
         modulus=shift%26
         shift=modulus
    
    for letter in text:
        if letter in alphabet:
            i=alphabet.index(letter)
            new_index= i + shift
            message += alphabet[new_index]
        else:
             message += letter
    
    print(f"the {direction}d text is {message}")





while True:

    direction=input("Type 'encode ' to encrypt, type 'decode ' to decrypt: \n")
    text=input("Type your message: \n").lower()
    shift=int(input("Type the shift number: \n"))
    ceaser(direction,text,shift)

    continue_choice =input("Do you want to continue Y or N ?").lower()

    if continue_choice != 'y' :
         print('Goodbye !!!!!')
         break

        
        
      