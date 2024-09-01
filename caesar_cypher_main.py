import caesar as cc
import art

print(art.logo)
print("\n==================================")

restart = True

while restart:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    print("----------------------------------")
    shift = int(input("Type the shift number:\n"))
    print("----------------------------------")

    if direction == 'encode' or direction == 'decode':
        cc.caesar(direction, text, shift)
    else: 
        print("Oops ... Unrecognized choice! Please type either 'encrypt' or 'decode' next time!😉")

    ending = input("Type 'yes' if you want to go again. Otherwise, type 'no'.\n")

    if ending == "no":
        restart = False
        "Goodbye!👋"
    else:
        print("Oops ... Unrecognized choice! Please type either 'yes' or 'no' next time when exiting the application!😉")

    
