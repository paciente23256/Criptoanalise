#!/usr/bin/python3
# -*- coding: utf-8 -*-
# IPBEJA - MESI-2021/2022 - CCA-Criptoanalise - Python
# Alunos #Rui #Pedro #Oscar
# Exercicio # 4 a) b)
import os, re


def print_tabela():
    tabela = ''
    for r in range(5):
        tabela += '\n'
        for c in range(5):
            tabela += tabela_main[r][c] + '\t'
    print(tabela)


# Funcao ve_tabela(letra) verifica se a letra ja existe na tabela
def ve_tabela(letra):
    ehlo = False
    exit = False
    for r in range(5):
        if exit == False:
            for c in range(5):
                if tabela_main[r][c] == letra:
                    ehlo = True
                    exit = True
                    break

    return ehlo


# Funcao celula_tabela(letra) define 1 celula na tabela para uma letra especifica
def celula_tabela(letra, nova_tabela):
    exit = False
    for r in range(5):
        if not exit:
            for c in range(5):
                if nova_tabela[r][c] == '*':
                    nova_tabela[r][c] = letra
                    exit = True
                    break


# Funcaoinit_tabela() inicia  a tabela com tudo [*]
def init_tabela():
    char = '*'
    for i in range(5):
        for j in range(5):
            tabela_main[i][j] = char
    return tabela_main


#Função limpa_chave_secreta(chave_secreta) altera chave_secreta para maiúsculas e substitui I por J
def limpa_chave_secreta(chave_secreta):
    # remove cracteres non-alpha 
    chave_secreta = re.sub(r'[^a-zA-Z]+', '', chave_secreta)
    # muda para maiusculas 
    chave_secreta = chave_secreta.upper()
    # substitui espacos por ""
    chave_secreta = chave_secreta.replace(" ", "")

    if chave_secreta:
        for J in chave_secreta:
            chave_secreta = chave_secreta.replace('J', 'I')

    print(chave_secreta)
    return chave_secreta


# Função para criar a tabela, primeiro insere a chave e depois adiciona o restante alfabeto
def criar_tabela(chave_secreta):
    # Obtem nova chave atraves função limpa_chave_secreta
    nova_chave_secreta = limpa_chave_secreta(chave_secreta)
    # Inicia a tabela para criar uma nova instância
    nova_tabela = init_tabela()

    # Adiciona a chave a tabela
    key_chars = []
    for char in nova_chave_secreta:
        if len(key_chars) == 0:
            key_chars.append(char)
        else:
            exist = False
            for c in key_chars:
                if c == char:
                    exist = True
                    break
            if exist == False:
                key_chars.append(char)

    for c in key_chars:
        celula_tabela(c, nova_tabela)

    tabela_main = nova_tabela
    for char in alphabet.upper():
        if ve_tabela(char) == False:
            celula_tabela(char, tabela_main)

    return (tabela_main)


def find_letra(letra):
    posicao = []
    for i in range(5):
        for j in range(5):
            if tabela_main[i][j] == letra:
                posicao = [i, j]
    return posicao


def limpa_msg_secreta(msg):
    # Remove espacos da msg
    msg = msg.upper()
    msg = msg.replace('J', 'I')
    msg = msg.replace(" ", "")
    nova_msg = []
    nova_msg = msg
    # Converte a lista para uma string de forma a poder manipular
    ch = []
    for cr in nova_msg:
        if len(ch) == 0:
            ch.append(cr)
        else:
            ch.append(cr)
    # Vai a msg e separa letras similares com um X ou um Q
    count = len(ch)
    for index in range(len(ch)):
        if index < count:
            ins_posicao = index + 1
            if ins_posicao < count:
                letra = ch[index]
                nova_letra = ch[ins_posicao]
                if nova_letra == letra and nova_letra != 'X':
                    ch.insert(ins_posicao, 'X')
                elif nova_letra == letra and nova_letra == 'X':
                    ch.insert(ins_posicao, 'Q')
                index += 1
    # Se o intervalo for um número ímpar e se foi adicionado um Z a uma string que terminou com Z, substitui o segundo Z por um Q
    if len(ch) % 2 != 0:
        if ch[len(ch) - 1] == 'Z':
            ch.append('Q')
        else:
            ch.append('Z')
    ch = ''.join(ch)
    print(ch)
    return ch


def encode_pair(l1, l2):
    posicao1 = find_letra(l1)
    posicao2 = find_letra(l2)
    row_a = posicao1[0]
    col_a = posicao1[1]
    row_b = posicao2[0]
    col_b = posicao2[1]
    # Caracteres da mesma linha
    if posicao1[0] == posicao2[0]:
        if col_a == 4:
            char1 = tabela_main[row_a][col_a - col_a]
            char2 = tabela_main[row_b][col_b + 1]
        elif col_b == 4:
            char1 = tabela_main[row_a][col_a + 1]
            char2 = tabela_main[row_b][col_b - col_b]
        else:
            char1 = tabela_main[row_a][col_a + 1]
            char2 = tabela_main[row_b][col_b + 1]
    # Caracteres da mesma coluna
    elif posicao1[1] == posicao2[1]:
        if row_a == 4:
            char1 = tabela_main[row_a - row_a][col_a]
            char2 = tabela_main[row_b + 1][col_b]
        elif row_b == 4:
            char1 = tabela_main[row_a + 1][col_a]
            char2 = tabela_main[row_b - row_b][col_b]
        else:
            char1 = tabela_main[row_a + 1][col_a]
            char2 = tabela_main[row_b + 1][col_b]
    # Codificação retangular
    else:
        char1 = tabela_main[row_a][col_b]
        char2 = tabela_main[row_b][col_a]
    pair = char1, char2
    pair = ''.join(pair)
    return pair


def decode_pair(l1, l2):
    posicao1 = find_letra(l1)
    posicao2 = find_letra(l2)
    row_a = posicao1[0]
    col_a = posicao1[1]
    row_b = posicao2[0]
    col_b = posicao2[1]
    # Caracteres da mesma linha
    if posicao1[0] == posicao2[0]:
        if col_a == 0:
            char1 = tabela_main[row_a][col_a + 4]
            char2 = tabela_main[row_b][col_b - 1]
        elif col_b == 0:
            char1 = tabela_main[row_a][col_a - 1]
            char2 = tabela_main[row_b][col_b + 4]
        else:
            char1 = tabela_main[row_a][col_a - 1]
            char2 = tabela_main[row_b][col_b - 1]
    # Caracteres da mesma coluna
    elif posicao1[1] == posicao2[1]:
        if row_a == 0:
            char1 = tabela_main[row_a + 4][col_a]
            char2 = tabela_main[row_b - 1][col_b]
        elif row_b == 0:
            char1 = tabela_main[row_a - 1][col_a]
            char2 = tabela_main[row_b + 4][col_b]
        else:
            char1 = tabela_main[row_a - 1][col_a]
            char2 = tabela_main[row_b - 1][col_b]
    # Codificação retangular
    else:
        char1 = tabela_main[row_a][col_b]
        char2 = tabela_main[row_b][col_a]
    pair = char1, char2
    pair = ''.join(pair)
    return pair


def encrypt(plaintext, chave_secreta):
    msg = plaintext
    criar_tabela(chave_secreta)
    print_tabela()
    nova_msg = limpa_msg_secreta(msg)
    final_msg = []
    for k in nova_msg:
        if len(nova_msg) > 0:
            l1 = nova_msg[:1]
            nova_msg = nova_msg[1:]
            l2 = nova_msg[:1]
            nova_msg = nova_msg[1:]
            new_pair = encode_pair(l1, l2)
            final_msg.append(new_pair)
            string1 = ''.join(final_msg)
    # Divide a mensagem cifrada em 5 X 5 caracteres
    cipher_text = ''
    x = 1
    for char in string1:
        cipher_text += char
        if x % 5 == 0:
            cipher_text += ' '
        x += 1

    print(cipher_text)


def decrypt(ciphertext, chave_secreta):
    msg = ciphertext.upper()
    msg = msg.replace(' ', '')
    criar_tabela(chave_secreta)
    print_tabela()
    final_msg = []
    string1 = ''
    x = 1
    for k in msg:
        while x < len(msg) + 1:
            l1 = msg[:1]
            msg = msg[1:]
            l2 = msg[:1]
            msg = msg[1:]
            new_pair = decode_pair(l1, l2)
            final_msg.append(new_pair)
            string1 = ''.join(final_msg)
            # x += 1
    # Divide a mensagem de texto em 5 X 5 caracteres
    plain_text = ''
    x = 1
    for char in string1:
        plain_text += char
        if x % 5 == 0:
            plain_text += ' '
        x += 1

    print(plain_text)


# Starting point
if __name__ == '__main__':
    while True:
        alphabet = 'abcdefghiklmnopqrstuvwxyz'  # J foi retirado
        secrata = []
        tabela_main = [['', '', '', '', ''],
                   ['', '', '', '', ''],
                   ['', '', '', '', ''],
                   ["", "", "", "", ""],
                   ['', '', '', '', '']]

        print("")
        print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
        print("| MESI2022 *CCA-PY* Exercicio nº. 4 a  b      |")
        #print("|     Playfair Cypher tool  Enc/Dec           | ")
        print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+\n")
        print("=> Escolha uma opção:")
        action = input('+ Playfair => Encrytar / Decryptar? [e/d] ')
        if action == 'e':
            chave_secreta = input('+ INSERIR A CHAVE: ')
            secret_msg = input('INSERIR A MSG (TEXTO): ')
            encrypt(secret_msg, chave_secreta)
        elif action == 'd':
            chave_secreta = input('+ Inserir a Chave para desencriptar a cifra: ')
            secret_cipher = input('Inserir a Cifra (texto) que quer desencriptar aqui: ')
            decrypt(secret_cipher, chave_secreta)
        else:
            print('+ opção inválida')
            break

        selection = input('+ Voltar a tentar... => Encrypt ou Decrypt? [y/n]')
        if selection == 'y':
            continue
        elif selection == 'n':
            break
        else:
            print('Opção inválida, O programa terminou')
            os.system('pause')
            break
