import alphabet as al

def encrypt(message, shift):
    #define original & encrypted text
    original_text = message.lower()
    # encrypted_text = [] #unused variable ... will be used if I decide to add a 'space' config or regex
    
    #create an encrypted alphabet
    al_len = len(al.alphabet)

    enc_text=""
    for ot_letter in original_text:
        #fetch the indices of the letters in the message
        ot_letter_index = al.alphabet.index(ot_letter)
        enc_letter = ot_letter_index+shift
        enc_letter%=al_len
        #feed the indices of the letters of the message to encrypt it using 'enc_letter'
        enc_text += al.alphabet[enc_letter]  

    print("\n==================================")
    print(f"Original Text: {original_text}" )
    print("----------------------------------")
    print(f"Encrypted Text: {enc_text}")
    print("==================================")
        
