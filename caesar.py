alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(direction, text, shift):
    message = text.lower()
    #create an encrypted alphabet
    al_len = len(alphabet)

    caesar_cipher = ""

    for letter in message: #fetch the indices of the letters in the message
        if letter in alphabet: 
            letter_index = alphabet.index(letter) # check what index in the alphabet is the current letter of the message is ...
            if direction == "decode":
                cc_letter = letter_index-shift 
            elif direction == "encode":
                cc_letter = letter_index+shift 
            cc_letter %= al_len
            #feed the indices of the letters of the message to encrypt it using 'enc_letter'
            caesar_cipher += alphabet[cc_letter]
        else:
            caesar_cipher += letter
    print("\n==================================")
    print(f"Original Text: {message}" )
    print("----------------------------------")
    print(f"{direction.capitalize()}d Text: {caesar_cipher}")
    print("==================================")

#caesar("decode", "difve", 4)
#difve encoded
#zebra decoded