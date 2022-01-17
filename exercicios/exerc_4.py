#!/usr/bin/python3
# -*- coding: utf-8 -*-
# IPBEJA - MESI-2021/2022 - CCA-Criptoanalise - Python
# Alunos #Rui #Pedro #Oscar
# Exercicio # 4 a) b)


print("")
print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
print("| MESI2022 *CCA-PY* Exercicio nº. 4 a  b      |")
print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+\n")
texto = input("+ Inserir texto [string] a cifrar: ")
num = int(input("+ Inserir numero para a chave: "))
texto = Cesar(texto, num)
print ("+ Texto cifrado:")
print(texto)
print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
