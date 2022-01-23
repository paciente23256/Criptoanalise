import numpy as np

digrafos = []  # Lista 2D, onde estarão os dígrafos
total = 0  # Variável acumuladora 
abc = ['A','B','C','D','E','F','G','H','I','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

# ------------------------------- Tabela Chave ------------------------------- #

# Função que irá verificar validade do input:
def inputString(mensagem):
    while True: 
        acum = 0 # Variável acumuladora

        string = str(input(mensagem))
        string = string.replace(' ','')
        string = string.upper()
        listString = list(string)
        if 'J' in listString:
            indice = listString.index('J')
            listString[indice] = 'I'
        
        for letra in listString:
            if letra in abc:
                acum += 1

        if acum == len(listString):
            return listString
        
        print('Input inválido')

palavraChave = inputString('Digite a palavra-chave: ')

c = palavraChave + abc  # Concatenação de listas
c = list(dict.fromkeys(c))  # Removendo valores que repetem definindo chaves de um dicionário, chaves sempre serão únicas

row1, row2, row3, row4, row5 = c[:5], c[5:10], c[10:15], c[15:20], c[20:25]

tabelaChave = np.array([row1,
                        row2,
                        row3,
                        row4,
                        row5])
                        
print(f'\n{tabelaChave}\n')

# ----------------------------------- Menu ----------------------------------- #

while True:
    modo = str(input(f'Digite 1 para Cifrar \nDigite 2 para Decifrar:'))
    if modo == '1' or modo == '2':
        break
    else:
        print('Input inválido')

# --------------------------------- Funções Gerais --------------------------------- #


def comparaComTabela(digrafo,length,linha1,coluna1,linha2,coluna2):
    global total

    if total == length: 
        return

    # Obtendo a localização do dígrafo atual da iteração dentro da lista de digrafos
    loc = np.where(np.all(digrafos == digrafo, axis=1))
    loc = np.unique(loc[0])
    total += len(loc)
    print(f'Digrafo a ser analisado: {digrafo}') 
    #print(f'loc: {loc}')
    
    if linha1 == linha2:
        print('Letras na mesma linha')
        
        if modo == '1':
            # Caso estejamos na última coluna
            if coluna1 == 4:
                coluna1 = -1
            if coluna2 == 4:
                coluna2 = -1
            
            a1 = tabelaChave[linha1][coluna1 + 1]
            a2 = tabelaChave[linha2][coluna2 + 1]
            # Caso tenhamos o mesmo digrafo repetido em diferentes posições da lista de digrafos:
            for i in loc:    
                resultado[i] = [a1,a2]
        else:
            # Caso estejamos na primeira coluna
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
            # Caso estejamos na última linha
            if linha1 == 4:
                linha1 = -1
            if linha2 == 4:
                linha2 = -1
            a1 = tabelaChave[linha1 + 1][coluna1]
            a2 = tabelaChave[linha2 + 1][coluna2]
            for i in loc:    
                resultado[i] = [a1,a2]
        else:
            # Caso estejamos na primeira linha
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
    # A fim de que o algoritmo não cifre/decifre algo que já foi cifrado, faremos uma cópia:
    resultado = digrafos.copy()
    digrafos = np.array(digrafos)
    length = len(digrafos)
    
    print(f'Lista de digrafos: {digrafos}')
    print()

    for digrafo in digrafos:
        # Encontrando cada letra do digrafo na tabela-chave
        firstLoc = np.where(tabelaChave == digrafo[0])
        secondLoc = np.where(tabelaChave == digrafo[1])
        linha1 = firstLoc[0][0]
        coluna1 = firstLoc[1][0]
        linha2 = secondLoc[0][0]
        coluna2 = secondLoc[1][0]
        
        comparaComTabela(digrafo,length,linha1,coluna1,linha2,coluna2)


# ---------------------------------Funções Específicas Cifragem --------------------------------- #

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
    lista = inputString('Digite a palavra a ser cifrada: ')
    percorreListaDigrafos(fazListaDigrafos(lista))


# --------------------------------- Decifragem --------------------------------- #

def decifrar():
    decif = inputString('Digite a palavra a ser decifrada: ')
    # Fazer lista de digrafos:
    for i in range(0,len(decif),2):
        digrafos.append([decif[i],decif[i+1]]) 
    percorreListaDigrafos(digrafos)

# ------------------------------------ Execução do Código ------------------------------------ #

if modo == '1':
    cifrar()
else:
    decifrar()

# Transformar lista em string:
txt = np.concatenate((digrafos))
txt = ''.join(txt)
resposta = np.concatenate((resultado))
resposta = ''.join(resposta)

print(f'Texto: {txt} --> Resultado: {resposta}')
