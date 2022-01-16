exit_program = False

alphabet = {
    "a": 0,
    "b": 1,
    "c": 2,
    "d": 3,
    "e": 4,
    "f": 5,
    "g": 6,
    "h": 7,
    "i": 8,
    "j": 9,
    "k": 10,
    "l": 11,
    "m": 12,
    "n": 13,
    "o": 14,
    "p": 15,
    "q": 16,
    "r": 17,
    "s": 18,
    "t": 19,
    "u": 20,
    "v": 21,
    "w": 22,
    "x": 23,
    "y": 24,
    "z": 25,
    "_": 26,
}


def encrypt(text, key):
    """Encrypts given text with given key using Vigenere's cipher """
    encrypted_text = ""
    # lowercase our text and remove whitespaces
    text = text.lower().replace(" ", "").replace("\n", "")
    key = key.lower().replace(" ", "").replace("\n", "")
    # encrypting whole text using Vigenere's cipher
    for el in range(len(text)):
        text_number = alphabet[text[el]]  # number assigned to specified letter
        key_number = alphabet[
            key[el % len(key)]
        ]  # we're looping using text length, so it's safe to use modulo if key's length is shorter
        encrypted_number = (
            text_number + key_number
        ) % 27  # finding number of new letter that will replace the original letter
        for alphabetkey, alphabetvalue in alphabet.items():
            if alphabetvalue == encrypted_number:
                encrypted_text += alphabetkey

    return encrypted_text


def decrypt(text, key):
    """ Decrypts given text that was encrypted with given key using Vigenere's cipher """
    decrypted_text = ""
    # lowercase and remove whitespaces in encrypted text and key
    text = text.lower().replace(" ", "").replace("\n", "")
    key = key.lower().replace(" ", "").replace("\n", "")
    for i in range(len(text)):
        text_number = alphabet[text[i]]  # index of encrypted text letter
        key_number = alphabet[key[i % len(key)]]  # index of key letter
        if text_number >= key_number:
            decrypted_number = text_number - key_number  # index of decrypted letter
            for alphakey, alphavalue in alphabet.items():
                if alphavalue == decrypted_number:
                    decrypted_text += alphakey  # writing decrypted letter into decrypted text
        else:
            # index of decrypted letter if index of key letter is greater than index of encrypted text
            decrypted_number = (27 - abs(text_number - key_number)) % 27
            for alphakey, alphavalue in alphabet.items():
                if alphavalue == decrypted_number:
                    decrypted_text += alphakey  # writing decrypted letter into decrypted text

    return decrypted_text


while not exit_program:
    print(
        """
    Welcome to Vingenere cipher program
    MENU:
        1. Encrypt message via terminal
        2. Decrypt message via terminal
        3. Encrypt message from file
        4. Decrypt message from file
        5. Exit
    """
    )
    answer = input("Choose option: ")
    if answer == "1":
        text = input("Enter the message you want to encrypt: ")
        key = input("Now enter the key you want to use: ")
        encrypted_message = encrypt(text, key)
        print("Encrypted message: " + encrypted_message + "\n")
        saveornottosave = input(
            "Do you want to save your message and key to file? Yes/No: ")
        saveornottosave = saveornottosave.lower()
        if saveornottosave == "yes" or saveornottosave == "y":
            filename = input("How to name your file? ")
            try:
                f = open(filename+".txt", "x")  # creates file under given name
                f.write(encrypted_message + "\n" + key)
                f.close()
            except:
                print("Error occured")
            else:
                print("File successfully created under '" + filename + "' name")
        else:
            continue
    elif answer == "2":
        text = input("Enter the message you want to decrypt: ")
        key = input("Now enter the key that was used to encrypt the message: ")
        decrypted_message = decrypt(text, key)
        print("Decrypted message: " + decrypted_message + "\n")
        saveornottosave = input(
            "Do you want to save your decrypted message and key to file? Yes/No: ")
        saveornottosave = saveornottosave.lower()
        if saveornottosave == "yes" or saveornottosave == "y":
            filename = input("How to name your file? ")
            try:
                f = open(filename+".txt", "x")  # creates file under given name
                f.write(decrypted_message + "\n" + key)
                f.close()
            except:
                print("Error occured")
            else:
                print("File successfully created under '" + filename + "' name")
        else:
            continue
    elif answer == "3":
        fname = input(
            "Enter the name of file which contains message and key: ")
        f = open(fname + ".txt")
        text = f.readline()
        key = f.readline()
        f.close()
        encrypted_message = encrypt(text, key)
        print("Encrypted message: " + encrypted_message + "\n")
        saveornottosave = input(
            "Do you want to save your encrypted message and key to file? Yes/No: ")
        saveornottosave = saveornottosave.lower()
        if saveornottosave == "yes" or saveornottosave == "y":
            filename = input("How to name your file? ")
            try:
                f = open(filename+".txt", "x")  # creates file under given name
                f.write(encrypted_message + "\n" + key)
                f.close()
            except:
                print("Error occured")
            else:
                print("File successfully created under '" + filename + "' name")
        else:
            continue
    elif answer == "4":
        fname = input(
            "Enter the name of file which contains encrypted message and key: ")
        f = open(fname + ".txt")
        text = f.readline()
        key = f.readline()
        f.close()
        decrypted_message = decrypt(text, key)
        print("Decrypted message: " + decrypted_message + "\n")
        saveornottosave = input(
            "Do you want to save your decrypted message and key to file? Yes/No: ")
        saveornottosave = saveornottosave.lower()
        if saveornottosave == "yes" or saveornottosave == "y":
            filename = input("How to name your file? ")
            try:
                f = open(filename+".txt", "x")  # creates file under given name
                f.write(decrypted_message + "\n" + key)
                f.close()
            except:
                print("Error occured")
            else:
                print("File successfully created under '" + filename + "' name")
        else:
            continue
    elif answer == "5":
        exit_program = True
    else:
        print("Error, please choose your option again")
        continue
