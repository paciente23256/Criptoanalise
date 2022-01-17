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
“fdrijrcxrufhlrekfufkvljrcjrfcrxizdrjuvgfiklxrcgfikvtilqridfjhlrekrjdrvjtyfirirdhlrekfjwzcyfjvdmrfivqrirdhlrekrjefzmrjwztrirdgfitrjrigrirhlvwfjjvjefjjffdrimrcvlrgverklufmrcvrgverjvrrcdrerfvgvhlverhlvdhlvigrjjrircvdufsfarufikvdhlvgrjjrircvdurufiuvljrfdrifgvizxfvfrszjdfuvldrjevcvvhlvvjgvcyflftvl”

R:
Posicao 25
"""
#modulo para o alfabeto
import string

def encrypt(text, shift):

    msg_encriptada = list(range(len(text)))
    alfabeto = string.ascii_lowercase # 'abcdefghijklmnopqrstuvwxyz'
    first_half = alfabeto[:shift]
    second_half = alfabeto[shift:]
    shifted_alfabeto = second_half + first_half

    for i, letra in enumerate(text.lower()):

        if letra in alfabeto:
            original_index = alfabeto.index(letra)
            nova_letra = shifted_alfabeto[original_index]
            msg_encriptada[i] = nova_letra
        else:
            msg_encriptada[i] = letra

    return "".join(msg_encriptada)

def decrypt(text, shift):
    """ quando a posicao ou mudanca e conhecida """
    decrypted_text = list(range(len(text)))
    alfabeto = string.ascii_lowercase
    first_half = alfabeto[:shift]
    second_half = alfabeto[shift:]
    shifted_alfabeto = second_half + first_half

    for i, letra in enumerate(text.lower()):

        if letra in alfabeto:
            index = shifted_alfabeto.index(letra)
            original_letra = alfabeto[index]
            decrypted_text[i] = original_letra
        else:
            decrypted_text[i] = letra

    return "".join(decrypted_text)

def brute_force_decrypt(text):
    """ Se a posicao/mudanca não for conhecida  """
    for n in range(26):
        print(f"Posição {n}")
        print(decrypt(text, n))
        print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")

print("")
print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
print("| MESI2022 *CCA-PY* Exercicio nº. 11   b      |")
print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+\n")
TEXTO = input("+ INSERIR MSG ADESENCRIPTAR: " )
key = int(input("+ ESCOLHA UMA CHAVE: " ))


#input_b = int(input())

print("")

#e = encrypt("texto fixo", 8)

# Encripta
e = encrypt(TEXTO , key)
# Decripta
print(decrypt(e, key))

# forca o e
brute_force_decrypt(e)
