#!/usr/bin/python3
# -*- coding: utf-8 -*-
# IPBEJA - MESI-2021/2022 - CCA-Criptoanalise - Python
# Alunos #Rui #Pedro #Oscar
# Exercicio # 4 a) b) - Cifra PlayFair


import numpy as np

"""
Biblioteca : modulo
O objeto principal do modulo numpy é o array multidimensional homogêneo. 
É uma tabela de elementos (geralmente números), todos do mesmo tipo, 
indexados por uma tupla (lista ordenada finita) de numeros inteiros positivos. 
neste modulo as dimensões são chamadas de eixos.

"""


digrafos = []  #  matriz lista, onde estarão os dígrafos
total = 0  # Variável acumulacao
alfabeto = ['A','B','C','D','E','F','G','H','I','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

"""
    Tabela
"""
# Função que verifica validade do input:
def inputString(mensagem):
    while True:
	
        print("\n+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
        print("|       MESI2022 *CCA - Criptoanalise*        |")
        print("|       Exercicio nº. 4 a e b - opcao 1       |")
        print("|              Cifra Play Fair                |")
        print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")

        acum = 0 # Variável de acumulacao
        string = str(input(mensagem))
        string = string.replace(' ','')
        string = string.upper()
        listString = list(string)
        if 'J' in listString:
            indice = listString.index('J')
            listString[indice] = 'I'

        for letra in listString:
            if letra in alfabeto:
                acum += 1

        if acum == len(listString):
            return listString

        print('Opção inválida')

chave = inputString('+ Inserir a Chave: ')

c = chave + alfabeto  # Concatenação de listas
c = list(dict.fromkeys(c))  # Remove valores repetidos define chaves únicas

row1, row2, row3, row4, row5 = c[:5], c[5:10], c[10:15], c[15:20], c[20:25]

"""
# modulo numpy

array([[ 0,  1,  2,  3,  4],
       [ 5,  6,  7,  8,  9],
       [10, 11, 12, 13, 14]])
       
"""
tabelaChave = np.array([row1,
                        row2,
                        row3,
                        row4,
                        row5])

print(f'\n{tabelaChave}\n')

"""
Menu input do utilizador
"""
while True:

    modo = str(input(f'Insira 1 para Cifrar \nInsira 2 para Decifrar: \n'))
    if modo == '1' or modo == '2':
        break
    else:
        print('+ opção invalida')
"""
Funcoes Gerais
"""

def comparaComTabela(digrafo,length,linha1,coluna1,linha2,coluna2):
    global total


    if total == length:
        return

    # Obter a localização do dígrafo atual da iteração dentro da lista de digrafos
    loc = np.where(np.all(digrafos == digrafo, axis=1))
    loc = np.unique(loc[0])
    total += len(loc)
    print(f'Digrafo analisado: {digrafo}')
    #print(f'loc: {loc}')

    if linha1 == linha2:
        print('Letras na mesma linha')

        if modo == '1':
            # no caso de estar na última coluna
            if coluna1 == 4:
                coluna1 = -1
            if coluna2 == 4:
                coluna2 = -1

            a1 = tabelaChave[linha1][coluna1 + 1]
            a2 = tabelaChave[linha2][coluna2 + 1]
            # no caso de obter digrafo repetido em diferentes posições da lista de digrafos:
            for i in loc:
                resultado[i] = [a1,a2]
        else:
            # na primeira coluna
            if coluna1 == 0:
                coluna1 = 5
            if coluna2 == 0:
                coluna2 = 5
            a1 = tabelaChave[linha1][coluna1 - 1]
            a2 = tabelaChave[linha2][coluna2 - 1]
            for i in loc:
                resultado[i] = [a1,a2]


    elif coluna1 == coluna2:
        print('Letras na mesma coluna')

        if modo == '1':
            # na última linha
            if linha1 == 4:
                linha1 = -1
            if linha2 == 4:
                linha2 = -1
            a1 = tabelaChave[linha1 + 1][coluna1]
            a2 = tabelaChave[linha2 + 1][coluna2]
            for i in loc:
                resultado[i] = [a1,a2]
        else:
            # na primeira linha
            if linha1 == 0:
                linha1 = 5
            if linha2 == 0:
                linha2 = 5
            a1 = tabelaChave[linha1 - 1][coluna1]
            a2 = tabelaChave[linha2 - 1][coluna2]
            for i in loc:
                resultado[i] = [a1,a2]

    else:
        print('Letras separadas na matriz, formar retângulo')

        distancia = coluna1 - coluna2
        a1 = tabelaChave[linha1][coluna1 - distancia]
        a2 = tabelaChave[linha2][coluna2 + distancia]
        for i in loc:
            resultado[i] = [a1,a2]
    print()

def percorreListaDigrafos(digrafos):
    global resultado
    # para q o algoritmo não cifre/decifre o que já foi cifrado, faz uma cópia:
    resultado = digrafos.copy()
    digrafos = np.array(digrafos)
    length = len(digrafos)

    print(f'Lista de digrafos: {digrafos}')
    print()

    for digrafo in digrafos:
        # Encontra cada letra do digrafo na tabela-chave
        firstLoc = np.where(tabelaChave == digrafo[0])
        secondLoc = np.where(tabelaChave == digrafo[1])
        linha1 = firstLoc[0][0]
        coluna1 = firstLoc[1][0]
        linha2 = secondLoc[0][0]
        coluna2 = secondLoc[1][0]

        comparaComTabela(digrafo,length,linha1,coluna1,linha2,coluna2)

"""
Funcoes especificas de encriptacao
"""
def fazListaDigrafos(lista):
    for i in range(0,len(lista),2):
        try:
            if lista[i] == lista[i+1]:
                lista.insert(i+1,'X')
            digrafos.append([lista[i],lista[i+1]])
        except IndexError:
            pass

    if len(lista) % 2 != 0:
        digrafos.append([lista[-1],'X'])

    return digrafos

def cifrar():
    lista = inputString('Inserir mesagem a cifrar: ')
    percorreListaDigrafos(fazListaDigrafos(lista))

"""
Decifra

"""

def decifrar():
    decif = inputString('Inserir mensagem a decifrar: ')
    # Fazer lista de digrafos:
    for i in range(0,len(decif),2):
        digrafos.append([decif[i],decif[i+1]])
    percorreListaDigrafos(digrafos)


"""Execucao do codigo"""
if modo == '1':
    cifrar()
else:
    decifrar()

"""Transformar lista em string"""
txt = np.concatenate((digrafos))
txt = ''.join(txt)
resposta = np.concatenate((resultado))
resposta = ''.join(resposta)

print(f'Texto: {txt} --> Resultado: {resposta}')
