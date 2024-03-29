'''
    caesar_break.py
    given caesar ciphertext, break cipher with frequency attack
'''



import string, sys, re



try:
    # auto mode: get ciphertext from opts
    raw_ciphertext = sys.argv[1]
except:
    # interactive: prompt user
    raw_ciphertext = input("Ciphertext to break: ")
    #raw_bruteforce = input("Launch a bruteforce attack?: (defaults no) ")
    raw_bruteforce = raw_ciphertext

print("")
ciphertext = raw_ciphertext.upper()
if (raw_bruteforce.upper()).find("Y") != -1:
    bruteforce = True
else:
    bruteforce = False

# check the frequency of each letter occurrence (A to Z)
for l in list(map(chr, range(ord('A'), ord('[')))):
    freq = ciphertext.count(l) / float(len(ciphertext.replace(" ", "")))
    # if letter appears 10% or more it could be 'E'
    if freq >= .1 or bruteforce:
        # shift so decrypt key is A=
        key = chr(ord(l) - 4)
        if ord(key) < 65:
            key = chr(ord(key) + 26)
        elif ord(key) > 90:
            key = chr(ord(key) - 26)

        print("Possible key: A=" + key + ". Attempting decryption...")
        print(decrypt(key, ciphertext) + "\n")






print("Numero de frequencias encontras no criptograma")
print("Letra E")
print(len(re.findall("e", raw_ciphertext)))
print("Letra O")
print(len(re.findall("o", raw_ciphertext)))
print("letra S")
print(len(re.findall("s", raw_ciphertext)))
print("letra R")
print(len(re.findall("r", raw_ciphertext)))
