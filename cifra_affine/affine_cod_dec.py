from string import ascii_lowercase
from secrets import SystemRandom
 
# Get the list of lowercase alphabet from a-z.
alphabets = list(ascii_lowercase)
# get the list of number from 0 to 25
numbers = [i for i in range(26)]
# pack the two lists into a dictionary.
# this is a reference table for encryption and decryption.
mapping_table = dict(zip(alphabets, numbers))
 
#############################################################################################################
# These two functions are directly copied from https://www.geeksforgeeks.org/implementation-affine-cipher/
# Extended Euclidean Algorithm for finding modular inverse
# eg: modinv(7, 26) = 15
def egcd(a, b):
    x, y, u, v = 0, 1, 1, 0
    while a != 0:
        q, r = b // a, b % a
        m, n = x - u * q, y - v * q
        b, a, x, y, u, v = a, r, u, v, m, n
    gcd = b
    return gcd, x, y
 
 
def modinv(a, m):
    gcd, x, y = egcd(a, m)
    if gcd != 1:
        return None  # modular inverse does not exist
    else:
        return x % m
#######################################################################################
 
# Below are original codes by myself, Affine cipher encryption formula:
# C = (a * P + b) mod 26, where C is cipher text, a is key1, P is plaintext, b is key2.
def affine_enc(key1, key2, plaintext):
    cursor = list()
    ciphertext = list()
    for p in plaintext:
        cursor.append((mapping_table[p] * key1 + key2) % 26)
    for c in cursor:
        for letter, num in mapping_table.items():
            if num == c:
 
                ciphertext.append(letter)
    return ''.join(ciphertext)
 
 
# Formula for Affine decryption:
# P = a^-1 (C - b) mod 26, where P is plaintext, a is key1, C is cipher text and b is key2.
# I have problem understanding the modulus inverse and hence copy and paste the two functions egcd and modinv directly
# from https://www.geeksforgeeks.org/implementation-affine-cipher/
def affine_decrypt(key1, key2, ciphertext):
    cursor = list()
    plaintext = list()
    for c in ciphertext:
        cursor.append((modinv(key1, 26) * (mapping_table[c] - key2)) % 26)
    for cur in cursor:
        for letter, num in mapping_table.items():
            if num == cur:
                plaintext.append(letter)
    return ''.join(plaintext)
 
 
if __name__ == "__main__":
    rng = SystemRandom()
    # Change your plaintext here
    plaintext = "iambadincryptomaths"
    # key1 is between 1 and 25.
    # key2 is between 1 and 25.
    # see this https://www.youtube.com/watch?v=_E8rSP0uAIY
    key1 = rng.randint(1, 25)
 
    # this is a test that the number must be gcd(a, 26) = 1 mod 26,
    # else try another number. where a is key1.
    while modinv(key1, 26) == None:
        key1 = rng.randint(1, 25)
    key2 = rng.randint(0, 25)
     
    print(f"Key1 is {key1}\n")
    print(f"Key2 is {key2}\n")
    print("Begin Affine Cipher...\n")
    ciphertext = affine_enc(key1, key2, plaintext.lower())
    print(f"This is the cipher text of {plaintext}: {ciphertext}\n")
    actual_plaintext = affine_decrypt(key1, key2, ciphertext)
    print(f"Decrypt {ciphertext}, the plaintext is {actual_plaintext}")
