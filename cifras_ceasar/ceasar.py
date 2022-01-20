from __future__ import annotations

from string import ascii_letters


def encrypt(mensagem: str, chave: int, alphabet: str | None = None) -> str:
    """
    Cifrar
    c = (x + n) % 26
    """
    # Define o alfabeto para caracteres minúsculos e maiúsculos
    alfabeto = alphabet or ascii_letters

    # resultado final da string
    result = ""

    for character in mensagem:
        if character not in alfabeto:
            # Anexa sem encriptar se o caracter não estiver no alfabeto
            result += character
        else:
            # Obtem o índice da nova chave e verifique se não é muito grande
            nova_chave = (alfabeto.index(character) + chave) % len(alfabeto)

            # Anexa o caracter encriptado ao alfabeto
            result += alfabeto[nova_chave]

    return result


def decrypt(mensagem: str, chave: int, alphabet: str | None = None) -> str:
    
    """
    Descifrar
    x = (c - n) % 26
    """
    # Torna o valor da chave negativo, inicia o decode
    chave *= -1

    return encrypt(mensagem, chave, alphabet)


def brute_force(mensagem: str, alphabet: str | None = None) -> dict[int, str]:
    """
    Força-Bruta
    
    """
    # Define o alfabeto para caracteres minúsculos e maiúsculos
    alfabeto = alphabet or ascii_letters

    # Armazena todos as combinacoes
    brute_force_data = {}

    # Percore todos as combinacoes
    for chave in range(1, len(alfabeto) + 1):
        # Descripta a mensagem e armazena os resultados em data
        brute_force_data[chave] = decrypt(mensagem, chave, alfabeto)

    return brute_force_data

if __name__ == "__main__":

    while True:
        print("")
        print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
        print("|       MESI2022 *CCA - Criptoanalise*        |")
        print("|       Exercicio nº. 3 a e b - opcao 1       |")
        print("|              Cifra de Caesar                |")
        print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
        print(*["1. Encriptar", "2. Desencriptar", "3. Brute-Force" , "0. Sair"], sep="\n")
        # input do utilizador
        choice = input("Escolha uma opção: ").strip() or "0"
          
        print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+\n")
        
    
        # executa as funcoes com base no input do utilizador
        if choice not in ("1", "2", "3", "0"):
            print("/!\ ERRO. Escolha uma opção válida.")
        elif choice == "1":
            mensagem = input("+ Inserir msg a Encriptar: ")
            chave = int(input("+ Inserir Chave: ").strip())

            print(encrypt(mensagem, chave))
        elif choice == "2":
            mensagem = input("+ Inserir msg a Desencriptar: ")
            chave = int(input("+ Inserir Chave: ").strip())

            print(decrypt(mensagem, chave))
        elif choice == "3":
            mensagem = input("+ Inserir msg a Desencriptar [Força-Bruta]: ")
            brute_force_data = brute_force(mensagem)

            for chave, value in brute_force_data.items():
                print(f"Chave: {chave} | Menssagem: {value}")

        elif choice == "0":
            print("Adeus.")
            break
