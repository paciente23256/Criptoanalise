#!/bin/python3
# Menu viginere
import runpy


"""
SHORT CUTS

"""
def go_encript():
    runpy.run_path('vigenere_enc.py')


def go_decript():
    runpy.run_path('vigenere_dec.py')



"""
MENU BANNER
"""
def showMenu():
    print ("\nCifra Vigenere")
    print ("-----------------")
    print ("1) Encriptar")
    print ("2) Decriptar")
    print ("3) Exit\n")
    data=int(input("Enter your choice: "))
    return data
data = showMenu()
while data!=3:
    user=showMenu()
    if data==1:
       go_encript() 
       #print("Files deleted")
    elif datat==2:
        go_decript()
        #print("Files created")
    elif user==3:
        print("Exiting")
    else:
        print("'%s' is an unknown option."%user)
