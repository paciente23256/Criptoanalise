#!/usr/bin/python3
# -*- coding: utf-8 -*-
# IPBEJA - MESI-2021/2022 - CCA-Criptoanalise - Python
# Alunos #Rui #Pedro #Oscar
# Exercicio # 3 a) b)

"""

Codifica uma determinada string (texto) com a cifra de césar e retornar mensagem encriptada

    Parâmetros:
    -----------
    * mensagem: o texto simples que precisa ser codificado
    * chave: o número de letras para deslocar a mensagem por


    output:
    * Uma string  texto cifrado/encriptado
    
    Sobre a cifra de César
    =========================
    A cifra de César tem o nome de Júlio César, que a usou ao enviar
    mensagens militares secretas para suas tropas. Esta é uma cifra de substituição simples
    onde cada caractere no texto simples é deslocado por um certo número conhecido
    como a "chave" ou "posicao".

    Exemplo:
    Digamos que temos a seguinte mensagem:
    "Olá, capitão"

    O alfabeto é composto de letras maiúsculas e minúsculas:
    "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

    E nosso turno é "2"

    Podemos então codificar a mensagem, uma letra de cada vez. "H" ficaria "J",
    já que "J" está a duas letras de distância, e assim por diante. Se a mudança 
    for superior a duas vezes, ou nossa letra estiver no final do alfabeto, voltamos ao inicio.
    ("Z" mudaria para "a" depois para "b" e assim por diante).

"""

from email import message
from string import ascii_letters


"""
Cifrar
c = (x + n) % 26
"""

def encrypt(message, chave):
    # Define o alfabeto para caracteres minúsculos e maiúsculos
    alfabeto = ascii_letters 
    # Resultado final da string
    result = ""
    for char in message:
        if char not in alfabeto:
            # Anexa sem encriptar se o caracter não estiver no alfabeto
            result += char
        else:
            # Obtem o índice da nova chave e verifique se não é muito grande
            nova_chave = (alfabeto.index(char) + chave) % len(alfabeto)
            # Anexa o caracter encriptado ao alfabeto
            result += alfabeto[nova_chave]
    return result
"""
Descifrar
x = (c - n) % 26
"""
def decrypt(message, chave):
    # Ativa o modo de desencriptacao torna a chave negativa
    return encrypt(message, (chave * -1))


"""
Brute-force
Cifra de Caesar.

"""

def brute_force():
    alfabeto = ascii_letters
    
    brute_force_data = {}
    
    for chave in range(1, len(alfabeto) + 1):
       
        brute_force_data[chave] = decrypt(message, chave, alfabeto)
        
    return brute_force_data


"""
banner - menu
"""
def main():
    while True:
        print("")
        print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
        print("|       MESI2022 *CCA - Criptoanalise*        |")
        print("|       Exercicio nº. 3 a e b - opcao 1       |")
        print("|              Cifra de Caesar                |")
        print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
        print(*["1. Encriptar", "2. Desencriptar", "3. Brute-Force" , "0. Sair"], sep="\n")

        user_choice = input("Escolha uma opção: ").strip() or "0"
        print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+\n")

        if user_choice not in ("1", "2", "3", "0"):
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
        elif user_choice == "3":
            message = input("+ Desencriptar Mensagem: ")
            brute_force_data = brute_force(message)
            for chave, value in brute_force_data.items():
                print(f"Chave: {chave} | Message: {value}")
        elif user_choice == "0":
            print("Obrigado.")
            break

if __name__ == "__main__":
    main()
