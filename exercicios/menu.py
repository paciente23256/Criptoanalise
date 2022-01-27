#!/usr/bin/python3
# -*- coding: utf-8 -*-
# IPBEJA - MESI-2021/2022 - CCA-Criptoanalise - Python
# Alunos #Rui #Pedro #Oscar
"""
MENU
"""

import subprocess, sys, os, runpy

"""atalhos"""


def go_cesar():
        runpy.run_path('cesar_tool.py')

def go_playfair():
        runpy.run_path('playfair_tool.py')

def go_railfence():
        runpy.run_path('railfence_tool.py')

def go_vigenere():
        runpy.run_path('vigenere_tool.py', run_name='__main__')

if __name__ == '__main__':

    subprocess.call('clear',shell=True)

    while True:
        print("")
        print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
        print("|       MESI2022 *CCA - Criptoanalise*        |")
        print("|            Oscar | Pedro | Rui              |")
        print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
        print(*["1. Cifra de Cesar Tool", "2. Cifra PlayFair Tool", "3. Cifra RailFence Tool" , "4. Cifra Vigenere Tool" , "0. Sair"], sep="\n")
        # input do utilizador
        choice = input("Escolha uma opção: ").strip() or "0"

        print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+\n")

        # executa as funcoes com base no input do utilizador
        if choice not in ("1", "2", "3", "4", "0"):
            print(" ! ERRO. Escolha uma opção válida.")
        elif choice == "1":
            go_cesar()
        elif choice == "2":
            go_playfair
        elif choice == "3":
            go_railfence
        elif choice == "4":
            go_vigenere
        elif choice == "0":
            print("Adeus.")
            break
        else:print("+ Selecione uma opção válida")
    print("+ Por favor tenta novamente")
