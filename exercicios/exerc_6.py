#!/usr/bin/python3
# -*- coding: utf-8 -*-
# IPBEJA - MESI-2021/2022 - CCA-Criptoanalise - Python
# Alunos #Rui #Pedro #Oscar
# Exercicio # 5 a) b) c) - Cifra Raifence

"""modulo de expressoes regulares"""
import re


"""
Funcao de cifra

Na cifra railfence, o texto simples é escrito diagonalmente para baixo em "trilhos"
sucessivos de uma grelha (matriz) imaginária, movendo-se para cima quando o trilho inferior
 é alcançado, para baixo novamente quando o trilho superior é alcançado e assim por diante até
 que todo o texto simples seja escrito Fora. O texto cifrado é então lido em rows.

Por exemplo, para criptografar a mensagem
'WE ARE DISCOVERED. RUN AT ONCE' com 3 "trilhos", escreva o texto como:

1   W . . . E . . . C . . . R . . . U . . . O . . .
2   . E . R . D . S . O . E . E . R . N . T . N . E
3   . . A . . . I . . . V . . . D . . . A . . . C .

"""

def cipher_encryption():
    msg = input("Inserir a msg: ")
    rails = int(input("Inserir o numero de  trilhos (linhas): "))

    # remove espacos da msg
    msg = msg.replace(" ", "")

    # cria uma matriz vazia
    railMatrix = []
    for i in range(rails):
        railMatrix.append([])
    for row in range(rails):
        for coluna in range(len(msg)):
            railMatrix[row].append('.')
        # inner for
    # for

    # testar a matriz
    #for row in railMatrix:
    #    for coluna in row:
    #        print(coluna, end="")
    #    print("\n")
    #    # inner for
    ## for

    # ordena as letras da msg em zig-zag na matriz
    row = 0
    check = 0
    for i in range(len(msg)):
        if check == 0:
            railMatrix[row][i] = msg[i]
            row += 1
            if row == rails:
                check = 1
                row -= 1
            # inner if
        elif check == 1:
            row -= 1
            railMatrix[row][i] = msg[i]
            if row == 0:
                check = 0
                row = 1
            # inner if
        # if-else

    # testa a matriz com a mensagem em zig-zag
    # for row in railMatrix:
    #     for coluna in row:
    #         print(coluna, end="")
    #     print("\n")
    #     # inner for
    # # for

    encryp_text = ""
    for i in range(rails):
        for j in range(len(msg)):
            encryp_text += railMatrix[i][j]
    # for

    # remove '.' do texto encriptado
    encryp_text = re.sub(r"\.", "", encryp_text)
    print("Encrypted Text: {}".format(encryp_text))


"""
Funcao Descifra

"""

def cipher_decryption():
    msg = input("Inserir a msg: ")
    rails = int(input("Inserir o numero de trilhos (linhas): "))

    # removing white space from message
    msg = msg.replace(" ", "")

    # creating an empty matrix
    railMatrix = []
    for i in range(rails):
        railMatrix.append([])
    for row in range(rails):
        for coluna in range(len(msg)):
            railMatrix[row].append('.')
        # inner for
    # for

    # testing the matrix
    # for row in railMatrix:
    #     for coluna in row:
    #         print(coluna, end="")
    #     print("\n")
    #     # inner for
    # # for

    # putting letters of message one by one in the matrix in zig-zag
    row = 0
    check = 0
    for i in range(len(msg)):
        if check == 0:
            railMatrix[row][i] = msg[i]
            row += 1
            if row == rails:
                check = 1
                row -= 1
                # inner if
        elif check == 1:
            row -= 1
            railMatrix[row][i] = msg[i]
            if row == 0:
                check = 0
                row = 1
            # inner if
        # if-else

    # testa a matriz com a msg em zig-zag
    # for row in railMatrix:
    #     for coluna in row:
    #         print(coluna, end="")
    #     print("\n")
    #     # inner for
    # # for

    # re ordena a matriz
    ordr = 0
    for i in range(rails):
        for j in range(len(msg)):
            temp = railMatrix[i][j]
            if re.search("\\.", temp):
                # skipping '.'
                continue
            else:
                railMatrix[i][j] = msg[ordr]
                ordr += 1
            # if-else
        # inner for
    # for

    # testa a re odernacao da matriz
    for i in railMatrix:
        for coluna in i:
            print(coluna, end="")
        #inner for
        print("\n")
    # for

    # mete a matriz reordenada num string desencriptada e retira o texto desencriptado
    check = 0
    row = 0
    decryp_text = ""
    for i in range(len(msg)):
        if check == 0:
            decryp_text += railMatrix[row][i]
            row += 1
            if row == rails:
                check = 1
                row -= 1
            # inner if
        elif check == 1:
            row -= 1
            decryp_text += railMatrix[row][i]
            if row == 0:
                check = 0
                row = 1
            # inner if
        # if-else
    # for

    decryp_text = re.sub(r"\.", "", decryp_text)


    print("MSg Desencriptada: {}".format(decryp_text))


def main():

  while True:

    print("\n+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
    print("|       MESI2022 *CCA - Criptoanalise*        |")
    print("|     Exercicio nº. 6 a b e c - opcao 1       |")
    print("|              Cifra Rail Fence               |")
    print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")


    choice = int(input("1. Encriptar\n2. Desencriptar\n0. Sair\nEscolha uma Opção: "))
    if choice == 1:
        print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
        cipher_encryption()
    elif choice == 2:
        print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
        cipher_decryption()
    elif choice == 0:
            print("Adeus.")
            break
    else:
        print("+ Opção ivalida")


if __name__ == "__main__":
    main()
