LETRAS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def main() -> None:

    print("")
    print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
    print("|              *Criptoanalise*                |")
    print("|                                             |")
    print("|              Cifra de vigenere              |")
    print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")


    mensagem = input("Inserir msg: ")
    chave = input("Inserir chave [alfanumerica]: ")
    modo = input("Encriptar/Desencriptar [e/d]: ")

    if modo.lower().startswith("e"):
        modo = "encripta"
        translated = enc_msg(chave, mensagem)
    elif modo.lower().startswith("d"):
        modo = "decripta"
        translated = dec_msg(chave, mensagem)

    print("\n%sed mensagem:" % modo.title())
    print(translated)


def enc_msg(chave: str, mensagem: str) -> str:
    """
 ENCRIPTA  
    """
    return translate_msg(chave, mensagem, "encripta")


def dec_msg(chave: str, mensagem: str) -> str:
    """
  DECRIPTA
    """
    return translate_msg(chave, mensagem, "decripta")


def translate_msg(chave: str, mensagem: str, modo: str) -> str:
    translated = []
    chaveIndex = 0
    chave = chave.upper()

    for symbol in mensagem:
        num = LETRAS.find(symbol.upper())
        if num != -1:
            if modo == "encripta":
                num += LETRAS.find(chave[chaveIndex])
            elif modo == "decripta":
                num -= LETRAS.find(chave[chaveIndex])

            num %= len(LETRAS)

            if symbol.isupper():
                translated.append(LETRAS[num])
            elif symbol.islower():
                translated.append(LETRAS[num].lower())

            chaveIndex += 1
            if chaveIndex == len(chave):
                chaveIndex = 0
        else:
            translated.append(symbol)
    return "".join(translated)


if __name__ == "__main__":
    main()