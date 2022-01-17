#!/usr/bin/python3
# -*- coding: utf-8 -*-
# IPBEJA - MESI-2021/2022 - CCA-Criptoanalise - Python
# Alunos #Rui #Pedro #Oscar
# Exercicio # 11 a) b)



"""

Para cifrar:
cesar -c -k 25 < texto-aberto.txt > texto-cifrado.txt

Para decifrar:
cesar -d -k 25 < texto-cifrado.txt > texto-aberto.txt

Opções:
-c : cifrar
-d : decifrar
-k n : valor da chave a ser usada

Exercicio
11. Tendo como referência a análise de frequências, desenvolva um programa em Python
que seja capaz de quebrar a Cifra de César:
a. Explique como funciona a análise de frequências e como esta pode ser aplicada
para quebrar a Cifra de César;

R:
A análise de frequências é uma técnica simples de criptanálise que consiste em identificar
os caracteres do texto cifrado usando a frequência de uso dos caracteres na língua em que
se supõe que a mensagem esteja escrita. O algoritmo de César é um cifrador de substituição 
simples e portanto vulnerável a essa técnica.

b. Descubra a mensagem original tendo como fonte o seguinte criptograma:
“fdrijrcxrufhlrekfufkvljrcjrfcrxizdrjuvgfiklxrcgfikvtilqridfjhlrekrjdrvjtyfirirdhlrekfjwz
cyfjvdmrfivqrirdhlrekrjefzmrjwztrirdgfitrjrigrirhlvwfjjvjefjjffdrimrcvlrgverklufmrcvr
gverjvrrcdrerfvgvhlverhlvdhlvigrjjrircvdufsfarufikvdhlvgrjjrircvdurufiuvljrfdrifgvizxf
vfrszjdfuvldrjevcvvhlvvjgvcyflftvl”

R:
Posicao 25 
"""
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

print("")
print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
print("| MESI2022 *CCA-PY* Exercicio nº. 11   b      |")
print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+\n")
TEXTO = input("+ INSERIR TEXTO ENC: " )
print("")
#e = encrypt("texto fixo", 8)
e = encrypt(TEXTO , 8)
# 'texto'
print(decrypt(e, 8))
# 'decrypta a bruta'
brute_force_decrypt(e)

