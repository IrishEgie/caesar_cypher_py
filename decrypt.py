import alphabet as al

def decrypt (message, shift):
    encrypted_text = message.lower()
    al_len = len(al.alphabet)

    original_text = ""
    for letter in encrypted_text:
        enc_letter_index = al.alphabet.index(letter)
        orginal_letter = enc_letter_index-shift
        orginal_letter %= al_len

        original_text += al.alphabet[orginal_letter]
    
    print("\n==================================")
    print(f"Encrypted Text: {encrypted_text}" )
    print("----------------------------------")
    print(f"Decrypted Text: {original_text}")
    print("==================================")



