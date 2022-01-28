import time, os, sys
import math
import re

status = ''
S = 'abcdefghijklmnopqrstuvwxyz'
l = len (S)


# Functions
def validate_status():
    m = input ('Please Enter the mode | 0 For Encrypt / 1 for Decrypt ')
    if m == '0':
        st = 'encrypt'
    elif m == '1':
        st = 'decrypt'
    else:
        m = input ('Invalid Value, again | Type: 0 For Encrypt / Type: 1 for Decrypt ')
    return st


def check2(b, l):
    if (b < 0) or (b > l - 1):
        sys.exit ('Key-2 must be between 0 and %s.' % (l - 1))


def check1(a, l):
    if (int (a) < 0):
        sys.exit ('Key-1 must be  be greater than 0 ')
    elif (math.gcd (int (a), l) != 1):
        sys.exit (
            ' The greatest Commun Division of Key-1 : %s and Length of Symbol List : %i must be equal to 1' % (a, l))


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


def affine_enc(msg, k1, k2, l):
    msg_encypted = ''
    for c in msg:
        if c in S:  # Only characters in 'S'
            c_index = S.index (c)  # Character's index

            c_dec_index = (c_index * k1 + k2) % l

            msg_encypted += S[c_dec_index]
        else:
            msg_encypted += c
    print ("# Key 1 :%s and Key 2: %s => %s " % (k1, k2, msg_encypted))
    return msg_encypted


def affine_dec(msg, k1, k2, l):
    inv_k1 = modinv (k1, l)
    msg_decypted = ''
    for c in msg:
        if c in S:  # Only characters in 'S'
            c_index = S.index (c)  # Character's index

            c_dec_index = (c_index - k2) * inv_k1 % l

            msg_decypted += S[c_dec_index]
        else:
            msg_decypted += c
    print ("# Key 1 :%s and Key 2: %s => %s " % (k1, k2, msg_decypted))
    return msg_decypted


def affine_cipher(msg, k1, k2, l, st):
    if st == 'encrypt':
        res = affine_enc (msg, k1, k2, l)
    elif st == 'decrypt':
        res = affine_dec (msg, k1, k2, l)

    return res


# Main

def Main():
    print ("****** THE AFFINE CIPHER || Encypting & Decrypting *******")
    print ('++ HOW IT WORKS +++')
    print ('+++    AFFINE CIPHER : C = key1 * P + key2    +++')
    print (
        '++++++++ C = Cipher Text Character (the necrypted message) , P =  PlainText character (the message) ++++++++')
    print ('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
    status = validate_status ()  # Encypting or Decrypting
    print ('\n')
    key1 = int (input ('Please Enter your Key1 '))
    print ('\n')
    check1 (key1, l)
    key2 = int (input ('Please Enter your Key2 '))
    print ('\n')
    check2 (key2, l)
    msg = input ('Please Enter your Message : ')
    print ('\n')
    # Infos
    print ('-------------All in All------------------')
    print ('List of symbols : %s ' % S)
    print ('\n')
    print ('Mode is : %s ' % status)
    print ('\n')
    print ('Key1 is : %s ' % key1)
    print ('\n')
    print ('Key2 is : %s ' % key2)
    print ('\n')
    print ('Your message is : %s ' % msg)
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
    r = affine_cipher (msg, key1, key2, l, status)
    t = round (time.time () - timer, 2)
    print ('The result is : %s' % r)
    print ('\n')
    print ('------------- SUMMARY ---------------------')
    print ('List of symbols : %s ' % S)
    print ('\n')
    print ('Mode is : %s ' % status)
    print ('\n')
    print ('Key1 is : %s ' % key1)
    print ('\n')
    print ('Key2 is : %s ' % key2)
    print ('\n')
    print ('Your message is : %s ' % msg)
    print ('\n')
    print ('The result is : %s ' % r)
    print ('\n')
    print ('Process time : %s ' % t)
    print ('\n')
    print ('-------------------------------------------')


if __name__ == '__main__':
    Main ()