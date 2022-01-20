#!/usr/bin/python3
# -*- coding: utf-8 -*-
# IPBEJA - MESI-2021/2022 - CCA-Criptoanalise - Python
# Alunos #Rui #Pedro #Oscar
# Exercicio # 3 a) b)

"""

 Cifra de Caesar
 É um tipo de cifra de substituição na qual cada letra do texto é substituída
 por outra, que se apresenta no alfabeto abaixo dela um número fixo de vezes.
 En(x)=(x+n)mod 26 -> Encriptar


"""

from string import ascii_letters


"""
 En(x)=(x+n)mod 26 -> Encriptar

"""
def encrypt(message, chave):
    alfabeto = ascii_letters
    result = ""
    for char in message:
        if char not in alfabeto:
            result += char
        else:
            nova_chave = (alfabeto.index(char) + chave) % len(alfabeto)
            result += alfabeto[nova_chave]
    return result
"""

 Dn(x)=(xi-n)mod 26 ->  Desencriptar

"""
def decrypt(message, chave):
    return encrypt(message, (chave * -1))

def main():
    while True:
        print("")
        print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
        print("|       MESI2022 *CCA - Criptoanalise*        |")
        print("|           Exercicio nº. 3 a e b             |")
        print("|              Cifra de Caesar                |")
        print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
        print(*["1. Encriptar", "2. Desencriptar", "0. Sair"], sep="\n")

        user_choice = input("Escolha uma opção: ").strip() or "0"
        print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+\n")

        if user_choice not in ("1", "2", "0"):
            print("! ERROR : Escolha uma opção válida!")
        elif user_choice == "1":
            message = input("+ Ecriptar Mensagem: ")
            chave = int(input("+ Inserir Chave: ").strip())
            print("\nMensagem Encriptada:")
            print(encrypt(message, chave))
        elif user_choice == "2":
            message = input("+ Desencriptar Mensagem: ")
            chave = int(input("+ Inserir Chave: ").strip())
            print("\nMensagem Desencriptada:")
            print(decrypt(message, chave))
        elif user_choice == "0":
            print("Obrigado.")
            break

if __name__ == "__main__":
    main()
