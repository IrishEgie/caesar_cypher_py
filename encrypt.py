import alphabet as al


def encrypt(message, shift):
    #define original & encrypted text
    original_text = message.lower()
    encrypted_text = [] 
    #original text length 
    ot_len = len(original_text)

    enc_al = [] # define blank encrypted alphabet

    #create an encrypted alphabet
    al_len = len(al.alphabet)

    #[enc]ypted_[l]etter_[batch number]_index
    for enc_l_1_index in range(shift, al_len):
        enc_letters_1 = al.alphabet[enc_l_1_index]
        enc_al.append(enc_letters_1)
        if enc_letters_1 == 'z':
            for enc_l_2_index in range (0, shift):
                enc_letters_2 = al.alphabet[enc_l_2_index]
                enc_al.append(enc_letters_2)

    enc_word=[]
    for ot_index in range (ot_len):
        ot_letter = original_text[ot_index]
        #fetch the indices of the letters in the message
        ot_letter_indices = al.alphabet.index(ot_letter)
        #feed the indices of the letters of the message to encrypt it using 'enc_al'
        enc_letter = enc_al[ot_letter_indices]
        #add the letters to the encrytped_text list
        enc_word.append(enc_letter)
        
    encrypted_word = ''.join(enc_word)
    print("\n==================================")
    print(f"Original Text: {original_text}" )
    print("----------------------------------")
    print(f"Encrypted Text: {encrypted_word}")
    print("----------------------------------")
    print(f"Encrpted Alphabet: {enc_al}")
    print("==================================")



        
