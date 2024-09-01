import encrypt as enc
import decrypt as dec

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
print("----------------------------------")
shift = int(input("Type the shift number:\n"))
print("----------------------------------")


# TODO-1: Create a function called 'encrypt()' that takes 'original_text' and 'shift_amount' as 2 inputs.
if direction == 'encode':
    enc.encrypt(text, shift)
elif direction == 'decode':
    dec.decrypt(text, shift)
else: 
    print("Oops ... Unrecognized choice! Please type either 'encrypt' or 'decode' next")
# TODO-2: Inside the 'encrypt()' function, shift each letter of the 'original_text' forwards in the alphabet
#  by the shift amount and print the encrypted text.

# TODO-4: What happens if you try to shift z forwards by 9? Can you fix the code?

# TODO-3: Call the 'encrypt()' function and pass in the user inputs. You should be able to test the code and encrypt a
#  message.

