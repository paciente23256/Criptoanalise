import affine_cipher
import time, os, sys
import math
import re

status = ''
S = 'abcdefghijklmnopqrstuvwxyz'
l = len (S)


# Functions

def validate_status():
    m = input ('Do you want to save the result in an Output File ? | 0 For YES / 1 for NO ')
    if m == '0':
        outputFile = input ('Please Enter your OutputFile location  : ')  # File's location (name)
        outputFile_status (outputFile)
        st = '0'
    elif m == '1':
        outputFile = None
        st = '1'
    else:
        m = input ('Invalid Value, again | Type: 0 For YES / Type: 1 for NO ')
    return st, outputFile


def outputFile_status(title):
    if os.path.lexists (title):
        print ('!! The file : %s already exist.You want to continue ? (Y)es or (N)o ? ' % (title))
        response = input ('> ')
        if not response.lower ().startswith ('y'):
            sys.exit ()


def writeFile(title, text):
    oFile = open (title, 'a+')
    oFile.write ("%s \n" % text)
    oFile.close ()


def makeKeys(k):
    key1 = k // l
    key2 = k % l
    return (key1, key2)


def egcd(A, B):
    if A == 0:
        return (B, 0, 1)
    else:
        g, y, x = egcd (B % A, A)
        return (g, x - (B // A) * y, y)


def modinv(a, m):
    g, x, y = egcd (a, m)
    if g != 1:
        raise Exception ('modular inverse does not exist')
    else:
        return x % m


def affine_dec(msg, k1, k2, l, status, oF):
    inv_k1 = modinv (k1, l)
    msg_decypted = ''
    for c in msg:
        if c in S:  # Only characters in 'S'
            c_index = S.index (c)  # Character's index

            c_dec_index = (c_index - k2) * inv_k1 % l

            msg_decypted += S[c_dec_index]
        else:
            msg_decypted += c
    if status == '0':
        print ("# Key 1 :%s and Key 2: %s => %s " % (k1, k2, msg_decypted))
        writeFile (oF, msg_decypted)
    return msg_decypted


def hack_affine(msg, l, status, oF):
    for k in range (l ** 2):
        k1 = makeKeys (k)[0]
        k2 = makeKeys (k)[1]
        if math.gcd (k1, l) != 1:
            continue
        dec_msg = affine_dec (msg, k1, k2, l, status, oF)
    return dec_msg


# Main

def Main():
    print ("****** HACKING || THE AFFINE CIPHER *******")
    print ('++ HOW IT WORKS +++')
    print ('+++    AFFINE CIPHER : C = key1 * P + key2    +++')
    print (
        '++++++++ C = Cipher Text Character (the encrypted message) , P =  PlainText character (Original message) ++++++++')
    print ('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
    (status, outputFile) = validate_status ()  # outputFile
    msg = input ('Please Enter your Message : ')
    print ('\n')
    # Infos
    print ('-------------All in All------------------')
    print ('List of symbols : %s ' % S)
    print ('\n')
    print ('Your message is : %s ' % msg)
    print ('\n')
    print ('Output File : %s ' % outputFile)
    print ('\n')
    print ('------------------------------------------')
    # Continue ?
    print ('You want to continue ? (Y)es or (N)o ?')
    response = input ('> ')
    if not response.lower ().startswith ('y'):
        sys.exit ()
    #
    print ('Processing now ...')
    timer = time.time ()
    hack_affine (msg, l, status, outputFile)
    t = round (time.time () - timer, 2)
    print ('-------------------------------------------')
    print ('Process time : %s ' % t)
    print ('\n')
    print ('-------------------------------------------')


if __name__ == '__main__':
    Main ()