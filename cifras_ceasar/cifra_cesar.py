#!/usr/bin/python3
# -*- coding: utf-8 -*-


"""Alfabeto lowercase """

#from string import ascii_lowercase #ascii_letters - minusc.
from string import ascii_uppercase #ascii_letters - maiusc

"""funcao encripta """
def encrypt(mensagem, chave):
    """
    Cifrar
    c = (x + n) % 26

    Escolhe a chave secreta (posicao) neste caso o "n" para cada letra no texto simples, e
    é substituida por uma letra do alfabeto que esteja a "n" letras de distância da letra.
    (Ex: para uma chave de 1, a se tornarva-se b, z tornarva-se a, etc.)

    encripta uma determinada string (texto) com a cifra de césar e retorna o codificado
    mensagem

    Parametros:
    -----------
    * menssage: texto simples que precisa ser codificado
    * key: número de letras para deslocar a mensagem

     Retorna:
    *   A string que contem o texto cifrado

    """
    # Define o alfabeto para caracteres minúsculos e maiúsculos

   #alfabeto = ascii_letters # os 2
    alfabeto = ascii_uppercase
   #alfabeto = ascii_lowercase

    # resultado final da string
    result = ""

    for character in mensagem:
        if character not in alfabeto:
            # Anexa sem encriptar se o caracter não estiver no alfabeto
            result += character
        else:
            # Obtem o índice da nova chave e verifique se não é muito grande
            nova_chave = (alfabeto.index(character) + chave) % len(alfabeto)

            # Anexa o caracter encriptado ao alfabeto
            result += alfabeto[nova_chave]

    return result

"""Funcao decripta"""
def decrypt(mensagem, chave):

    """
    Descifrar
    x = (c - n) % 26

    Parametros:
    -----------
    *   menssage: texto simples que precisa ser descodificado
    *   key: the number of letters to shift the message backwards by to decode
    Retorna:
    *   A string containing the decoded plain-text

    """
    # Torna o valor da chave negativo, inicia o decode
    chave *= -1

    return encrypt(mensagem, chave)


"""Funcao brute force"""
def brute_force(mensagem):
    """
    Força-Bruta:
    ------------
    Retorna todas as combinações possíveis de chaves e as strings decodificadas no
    forma de dicionário

    Parametros:
    -----------
    * message: o texto cifrado a ser usado durante a força bruta
    |
    -----------
    Força bruta é quando uma pessoa intercepta uma mensagem ou senha, sem saber
    a chave e tenta todas as combinações. Com a cifra de césar torna-se fácil,
    uma vez que estamos limitados as letras do alfabeto.
    Quanto maior for a complexidade da cifra , maior sera o tempo levado a fazer força bruta.
    """
    # Define o alfabeto para caracteres minúsculos e maiúsculos
    alfabeto = ascii_uppercase

    # Armazena todos as combinacoes
    brute_force_data = {}

    # Percore todos as combinacoes
    for chave in range(1, len(alfabeto) + 1):
        # Descripta a mensagem e armazena os resultados em data
        brute_force_data[chave] = decrypt(mensagem, chave)

    return brute_force_data

if __name__ == "__main__":

    while True:
        print("")
        print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
        print("|              Cifra de Caesar                |")
        print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
        print(*["1. Cifrar", "2. Decifrar", "3. Brute-Force" , "0. Sair"], sep="\n")
        # input do utilizador
        choice = input("Escolha uma opção: ").strip() or "0"

        print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+\n")


        # executa as funcoes com base no input do utilizador
        if choice not in ("1", "2", "3", "0"):
            print(" ! ERRO. Escolha uma opção válida.")
        elif choice == "1":
            mensagem = input("+ Inserir msg a Encriptar: ").upper()
            chave = int(input("+ Inserir Chave: ").strip())

            print(encrypt(mensagem, chave))
        elif choice == "2":
            mensagem = input("+ Inserir msg a Desencriptar: ").upper()
            chave = int(input("+ Inserir Chave: ").strip())

            print(decrypt(mensagem, chave))
        elif choice == "3":
            mensagem = input("+ Inserir msg a Desencriptar [Força-Bruta]: ").upper()
            brute_force_data = brute_force(mensagem)

            for chave, value in brute_force_data.items():
                print(f"Chave: {chave} | Menssagem: {value}")

        elif choice == "0":
            print("Adeus.")
            break
