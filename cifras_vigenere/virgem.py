

def encrypt(plaintext, key):
    key_length = len(key)
    key_as_int = [ord(i) for i in key]
    plaintext_int = [ord(i) for i in plaintext]
    ciphertext = ''
    for i in range(len(plaintext_int)):
        value = (plaintext_int[i] + key_as_int[i % key_length]) % 26
        ciphertext += chr(value + 65)
    return ciphertext


def decrypt(ciphertext, key):
    key_length = len(key)
    key_as_int = [ord(i) for i in key]
    ciphertext_int = [ord(i) for i in ciphertext]
    plaintext = ''
    for i in range(len(ciphertext_int)):
        value = (ciphertext_int[i] - key_as_int[i % key_length]) % 26
        plaintext += chr(value + 65)
    return plaintext


if __name__ == "__main__":

    while True:
        print("")
        print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
        print("|              Cifra de Vigenere              |")
        print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
        print(*["1. Encriptar", "2. Desencriptar",  "0. Sair"], sep="\n")
        # input do utilizador
        choice = input("Escolha uma opção: ").strip() or "0"

        print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+\n")

        # executa as funcoes com base no input do utilizador
        if choice not in ("1", "2", "0"):
            print(" ! ERRO. Escolha uma opção válida.")
        elif choice == "1":
            plaintext = input("+ Inserir msg a Encriptar: ")
            key = int(input("+ Inserir Chave: ").strip())
            print(encrypt(plaintext, key))
        elif choice == "2":
            ciphertext = input("+ Inserir msg a Desencriptar: ")
            key = int(input("+ Inserir Chave: ").strip())

            print(decrypt(ciphertext, key))
        
        elif choice == "0":
            print("Adeus.")
            break
