
#!/usr/bin/python3
# -*- coding: utf-8 -*-
# IPBEJA - MESI-2021/2022 - CCA-Criptoanalise - Python
# Alunos #Rui #Pedro #Oscar
# Cifra Affine Tool

import sys, time
import os

# This function calculates the modular inverse of a number
def mod_inv (num, mod):
    for x in range(0,mod + 1):
        if ((num*x)%mod == 1):
            return x
    sys.exit('[!!!] ERROR: modulo %d inverse of %d does not exists!' % (mod, num))

# Checking arguments
if len(sys.argv) > 1 and (sys.argv[1] == '-h' or sys.argv[1] == '--help'):
    sys.exit('excutar brute force a mes inserida' % sys.argv[0])

# Reading file and setting output file
print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
print("|       MESI2022 *CCA - Criptoanalise*        |")
print("|            Oscar | Pedro | Rui              |")
print("|         *Cifra de Affine - Tool*            |")
print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
print("+ Ataque - Força Bruta")
msg = input('\n+ Inserir Mensagem/criptograma: ')
# escreve ficheiro
exploit = open('exploit.txt','w')
exploit.write('*** Chaves Testadas ***\n');
# tempo inicial
timer = time.time ()
# Brute force algorithm
for i in range(0,26):
    if (i%2 != 0) and (i != 13):
        for j in range(0,26):
            exploit.write('\n# Chave usada <%d,%d>\n# Mensagem : ' % (i,j))
            inv = mod_inv(i,26)
            for c in msg:
                v = ord(c)
                if (v >= 65) and (v <= 90):
                    # maiusc.
                    cip = ((v - 65 - j)*inv + 26)%26 + 65
                elif (v >= 97) and (v <= 122):
                    # minusc.
                    cip = ((v - 97 - j)*inv + 26)%26 + 97
                else:
                    # outros caract
                    cip = v
                # decifra escreve no ficheiro o resultado               
                
                exploit.write('%c' % cip)
                # tempo final
                t = round (time.time () - timer, 2)
               
with open('exploit.txt', 'r') as log:
     print(''.join(log.readlines()))
     print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
     print ('Tempo de processamento : %s ' % t)
     print ('\n') 
     print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")

