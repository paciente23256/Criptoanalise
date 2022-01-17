#!/usr/bin/python3
# -*- coding: utf-8 -*-
# IPBEJA - MESI-2021/2022 - CCA-Criptoanalise - Python
# Alunos #Rui #Pedro #Oscar
# Exercicio # 3 a) b)

def Cesar(texto, num):
    alfabeto = [chr(i) for i in range(97,123)]
    converter_texto_list = []
    converter_texto = ""
    was_uppercase = False
    for caracter in texto:
        if caracter.isupper():
            caracter = caracter.lower()
            was_uppercase = True
        if caracter not  in alfabeto:
            converter_texto = converter_texto_list.append(caracter)
            continue
        carac_convertido_num = (alfabeto.index(caracter) + num)%26
        carac_convertido = alfabeto[carac_convertido_num]
        if was_uppercase:
            converter_texto_list.append(carac_convertido.upper())
            was_uppercase = False
        else:
            converter_texto_list.append(carac_convertido)
    converter_texto = "".join(converter_texto_list)
    return converter_texto

print("")
print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
print("| MESI2022 *CCA-PY* Exercicio nº. 3 a  b      |")
print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+\n")
texto = input("+ Inserir texto [string] a cifrar: ")
num = int(input("+ Inserir numero para a chave: "))
texto = Cesar(texto, num)
print ("+ Texto cifrado:")
print(texto)
print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
