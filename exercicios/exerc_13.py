#!/usr/bin/python3
# -*- coding: utf-8 -*-
# IPBEJA - MESI-2021/2022 - CCA-Criptoanalise - Python
# Alunos #Rui #Pedro #Oscar
# Exercicio # 13 a) - Cifra de vigenere  - Cifra.

LETRAS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def main() -> None:
  while True:

    print("")
    print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
    print("|       MESI2022 *CCA - Criptoanalise*        |")
    print("|           Exercicio nº. 5 a e b             |")
    print("|              Cifra de vigenere              |")
    print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
    modo = input("e. Encriptar\nd. Desencriptar\nEscolha uma Opção: ")
    mensagem = input("Inserir msg: ")
    chave = input("Inserir chave [alfanumerica]: ")

    if modo.lower().startswith("d"):
        modo = "encripta"
        translated = enc_msg(chave, mensagem)
    elif modo.lower().startswith("e"):
        modo = "decripta"
        translated = dec_msg(chave, mensagem)

    print("\n%sed mensagem:" % modo.title())
    print(translated)


def enc_msg(chave: str, mensagem: str) -> str:
    """
 ENCRIPTA
    """
    return translate_msg(chave, mensagem, "encripta")


def dec_msg(chave: str, mensagem: str) -> str:
    """
  DECRIPTA
    """
    return translate_msg(chave, mensagem, "decripta")


def translate_msg(chave: str, mensagem: str, modo: str) -> str:
    translated = []
    chaveIndex = 0
    chave = chave.upper()

    for symbol in mensagem:
        num = LETRAS.find(symbol.upper())
        if num != -1:
            if modo == "encripta":
                num += LETRAS.find(chave[chaveIndex])
            elif modo == "decripta":
                num -= LETRAS.find(chave[chaveIndex])

            num %= len(LETRAS)

            if symbol.isupper():
                translated.append(LETRAS[num])
            elif symbol.islower():
                translated.append(LETRAS[num].lower())

            chaveIndex += 1
            if chaveIndex == len(chave):
                chaveIndex = 0
        else:
            translated.append(symbol)
    return "".join(translated)


if __name__ == "__main__":
    main()
