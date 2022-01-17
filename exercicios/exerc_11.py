#!/usr/bin/python3
# -*- coding: utf-8 -*-
# IPBEJA - MESI-2021/2022 - CCA-Criptoanalise - Python
# Alunos #Rui #Pedro #Oscar
# Exercicio # 11 a) b)
# Usar cifra de ceasar



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
"omarsalgadoquantodoteusalsaolagrimasdeportugalportecruzarmosquantasmaeschoraramquantosfilhosemvaorezaramquantasnoivasficaramporcasarparaquefossesnossoomarvaleuapenatudovaleapenaseaalmanaoepequenaquemquerpassaralemdobojadortemquepassaralemdadordeusaomaroperigoeoabismodeumasneleequeespelhouoceu"
"""

""" INICIO DO CODIGO """

#modulo para o alfabeto
import string

"""
Encrypt

"""
def encripta(text, shift):

    texto_encriptado = list(range(len(text)))
    alfabeto = string.ascii_lowercase # 'abcdefghijklmnopqrstuvwxyz'
    primeira_metade = alfabeto[:shift]
    segunda_metade = alfabeto[shift:]
    shifted_alfabeto = segunda_metade + primeira_metade

    for i, letra in enumerate(text.lower()):

        if letra in alfabeto:
            original_index = alfabeto.index(letra)
            nova_letra = shifted_alfabeto[original_index]
            texto_encriptado[i] = nova_letra
        else:
            texto_encriptado[i] = letra

    return "".join(texto_encriptado)


"""
Decrypt

"""
def desencripta(texto, shift):
    """ quando a posicao ou mudanca e conhecida """
    texto_desencriptado = list(range(len(texto)))
    alfabeto = string.ascii_lowercase
    primeira_metade = alfabeto[:shift]
    segunda_metade = alfabeto[shift:]
    shifted_alfabeto = segunda_metade + primeira_metade

    for i, letra in enumerate(texto.lower()):

        if letra in alfabeto:
            index = shifted_alfabeto.index(letra)
            letra_original = alfabeto[index]
            texto_desencriptado[i] = letra_original
        else:
            texto_desencriptado[i] = letra

    return "".join(texto_desencriptado)

"""
Brute-Force

"""
def desencripta_bforce(texto):
    """ Se a posicao/mudanca não for conhecida  """
    for n in range(26):
        print(f"Posição / Mudança {n}")
        print(desencripta(texto, n))
        print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")

print("")
print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
print("| MESI2022 *CCA-PY* Exercicio nº. 11   b      |")
print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+\n")
msg = input("+ INSERIR MSG A DESENCRIPTAR: " )
key = int(input("+ ESCOLHA UMA CHAVE: " ))

#ecripta texto e chave previamente definida # sem input do utilizador
#e = encripta("xrtetxto0 xfixoth", 8)

e = encripta(msg , key)
desencripta_bforce(e)

print("\n+ MENSAGEM INSERIDA:")
print(desencripta(e, key))

print("+ CHAVE USADA:")
print(key)

print("\n+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
