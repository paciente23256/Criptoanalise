import string

def encrypt(text, shift):

    encrypted_text = list(range(len(text)))
    alphabet = string.ascii_lowercase # 'abcdefghijklmnopqrstuvwxyz'
    first_half = alphabet[:shift]
    second_half = alphabet[shift:]
    shifted_alphabet = second_half + first_half
    
    for i, letter in enumerate(text.lower()):

        if letter in alphabet:
            original_index = alphabet.index(letter)
            new_letter = shifted_alphabet[original_index]
            encrypted_text[i] = new_letter    
        else:
            encrypted_text[i] = letter

    return "".join(encrypted_text)

def decrypt(text, shift):
    """ when the shift is known """
    decrypted_text = list(range(len(text)))
    alphabet = string.ascii_lowercase
    first_half = alphabet[:shift]
    second_half = alphabet[shift:]
    shifted_alphabet = second_half + first_half
    
    for i, letter in enumerate(text.lower()):

        if letter in alphabet:
            index = shifted_alphabet.index(letter)
            original_letter = alphabet[index]
            decrypted_text[i] = original_letter 
        else:
            decrypted_text[i] = letter

    return "".join(decrypted_text)

def brute_force_decrypt(text):
    """ when the shift is unknown """
    for n in range(26):
        print(f"Using a shift value of {n}")
        print(decrypt(text, n))
        print("\n***\n")
 
e = encrypt("how now brown cow", 8)
# 'pwe vwe jzwev kwe'
print(decrypt(e, 8))
# 'how now brown cow'
brute_force_decrypt(e)
"""Using a shift value of 0
pwe vwe jzwev kwe

***

Using a shift value of 1
ovd uvd iyvdu jvd

***

Using a shift value of 2
nuc tuc hxuct iuc

***

Using a shift value of 3
mtb stb gwtbs htb

***

Using a shift value of 4
lsa rsa fvsar gsa

***

Using a shift value of 5
krz qrz eurzq frz

***

Using a shift value of 6
jqy pqy dtqyp eqy

***

Using a shift value of 7
ipx opx cspxo dpx

***

Using a shift value of 8
how now brown cow

***

Using a shift value of 9
gnv mnv aqnvm bnv

***

Using a shift value of 10
fmu lmu zpmul amu

***

Using a shift value of 11
elt klt yoltk zlt

***

Using a shift value of 12
dks jks xnksj yks

***

Using a shift value of 13
cjr ijr wmjri xjr

***

Using a shift value of 14
biq hiq vliqh wiq

***

Using a shift value of 15
ahp ghp ukhpg vhp

***

Using a shift value of 16
zgo fgo tjgof ugo

***

Using a shift value of 17
yfn efn sifne tfn

***

Using a shift value of 18
xem dem rhemd sem

***

Using a shift value of 19
wdl cdl qgdlc rdl

***

Using a shift value of 20
vck bck pfckb qck

***

Using a shift value of 21
ubj abj oebja pbj

***

Using a shift value of 22
tai zai ndaiz oai

***

Using a shift value of 23
szh yzh mczhy nzh

***

Using a shift value of 24
ryg xyg lbygx myg

***

Using a shift value of 25
qxf wxf kaxfw lxf

***"""
