
def Cesar(text, num):
    alphabet = [chr(i) for i in range(97,123)]
    text_converted_list = []
    text_converted = ""
    was_uppercase = False
    for caracter in text:
        if caracter.isupper():
            caracter = caracter.lower()
            was_uppercase = True
        if caracter not  in alphabet:
            text_converted = text_converted_list.append(caracter)
            continue
        carac_converted_num = (alphabet.index(caracter) + num)%26
        carac_converted = alphabet[carac_converted_num]
        if was_uppercase:
            text_converted_list.append(carac_converted.upper())
            was_uppercase = False
        else:
            text_converted_list.append(carac_converted)
    text_converted = "".join(text_converted_list)
    return text_converted

text = input("Insert a text to Chiper: ")
num = int(input("Choose a key number: "))
text = Cesar(text, num)
print(text)
