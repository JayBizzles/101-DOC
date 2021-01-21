import art

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
alphabet = alphabet * 2
print(art.logo)
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n\n"))

if shift > 25:
    shift = shift % 25


#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.

# def encrypt(plain_text, shift_amount):
#     cipher_block = []
#     for letter in text:
#         current_pos = alphabet.index(letter)
#         new_pos = current_pos + shift
#         cipher_block.append(alphabet[new_pos])

#     secret_text = ''.join(cipher_block)
#     print(f"The plain text: {text}\n")

#     print(f"The cipher text: {secret_text}\n")

    #TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.  
    #e.g. 
    #plain_text = "hello"
    #shift = 5
    #cipher_text = "mjqqt"
    #print output: "The encoded text is mjqqt"

    ##HINT: How do you get the index of an item in a list:
    #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

    ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

    #TODO-3: Create a different function called 'decrypt' that takes the 'text' and 'shift' as inputs.
# def decrypt(plain_text, shift_amount):
#     cipher_block = []
#     for letter in text:
#         current_pos = alphabet.index(letter)
#         new_pos = current_pos - shift
#         cipher_block.append(alphabet[new_pos])

#     secret_text = ''.join(cipher_block)
#     print(f"The plain text: {text}\n")

#     print(f"The cipher text: {secret_text}\n")

    #TODO-4: Inside the 'decrypt' function, shift each letter of the 'text' *backwards* in the alphabet by the shift amount and print the decrypted text.  
    #e.g. 
    #cipher_text = "mjqqt"
    #shift = 5
    #plain_text = "hello"
    #print output: "The decoded text is hello"


    #TODO-5: Check if the user wanted to encrypt or decrypt the message by checking the 'direction' variable. Then call the correct function based on that 'drection' variable. You should be able to test the code to encrypt *AND* decrypt a message.

# if direction == 'encode':
#     encrypt(plain_text=text, shift_amount=shift)
# elif direction == 'decode':
#     decrypt(plain_text=text, shift_amount=shift)
# else:
#     print("Error: Input the correct value")

    #TODO-6: Combine the encrypt() and decrypt() functions into a single function called caesar().

def ceasar(plain_text = text,shift_number = shift,direction = direction):
    cipher_block = ''
    if direction == 'encode':
        for letter in plain_text:
            if letter not in alphabet:
                cipher_block+=letter
            else:
                current_pos = alphabet.index(letter)
                new_pos = current_pos + shift_number
                cipher_block+=alphabet[new_pos]

        secret_text = cipher_block
        print(f"The plain text: {plain_text}\n")

        print(f"The cipher text: {secret_text}\n")
    elif direction == 'decode':
        for letter in plain_text:
            if letter not in alphabet:
                cipher_block+=letter
            else:
                current_pos = alphabet.index(letter)
                new_pos = current_pos - shift_number
                cipher_block+=alphabet[new_pos]

        secret_text = cipher_block    
        print(f"The plain text: {plain_text}\n")

        print(f"The cipher text: {secret_text}\n")
    else:
        print("Error: Input the correct value")
    choice = input("Would you like to restart the cipher?(y/n)")
    if choice == 'y':
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n\n"))
        if shift > 25:
            shift = shift % 25
        ceasar(text,shift,direction)



#TODO-7: Call the caesar() function, passing over the 'text', 'shift' and 'direction' value

ceasar(text,shift,direction)

