#Verifica todas as possibilidades ou posicoes do alfabeto

#import pyfiglet
import string

def encrypt(text, shift):

    encrypted_text = list(range(len(text)))
    alphabet = string.ascii_lowercase # 'abcdefghijklmnopqrstuvwxyz'
    first_half = alphabet[:shift]
    second_half = alphabet[shift:]
    shifted_alphabet = second_half + first_half

    for i, letter in enumerate(text.lower()):

        if letter in alphabet:
            original_index = alphabet.index(letter)
            new_letter = shifted_alphabet[original_index]
            encrypted_text[i] = new_letter
        else:
            encrypted_text[i] = letter

    return "".join(encrypted_text)

def decrypt(text, shift):
    """ quando a posicao ou mudanca e conhecida """
    decrypted_text = list(range(len(text)))
    alphabet = string.ascii_lowercase
    first_half = alphabet[:shift]
    second_half = alphabet[shift:]
    shifted_alphabet = second_half + first_half

    for i, letter in enumerate(text.lower()):

        if letter in alphabet:
            index = shifted_alphabet.index(letter)
            original_letter = alphabet[index]
            decrypted_text[i] = original_letter
        else:
            decrypted_text[i] = letter

    return "".join(decrypted_text)

def brute_force_decrypt(text):
    """ Se a posicao/mudanca não for conhecida  """
    for n in range(26):
        #print(" +-+-+-+-+-+-+ +-+ +-+-+-+-+-+\n")
        print(f"Posicao {n}")
        print(decrypt(text, n))
        print(" +-+-+-+-+-+-+ +-+ +-+-+-+-+-+\n")

print("\n+-+-+-+-+-+-+ +-+ +-+-+-+-+-+")
print(" |C|E|A|S|A|R| |A| |B|R|U|T|A|")
print(" +-+-+-+-+-+-+ +-+ +-+-+-+-+-+\n")
TEXTO = input("+ INSERIR TEXTO: " )
print("")
#e = encrypt("texto fixo", 8)
e = encrypt(TEXTO , 8)
# 'texto'
print(decrypt(e, 8))
# 'decrypta a bruta'
brute_force_decrypt(e)

