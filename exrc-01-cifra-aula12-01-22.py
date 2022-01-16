def main():
    mensagem = "BOA NOITE A TODOS"
    chave = [5, 1]

    criptograma = affine_cifra(mensagem, chave)

    print('Mensagem Cifrada: {}'.format( criptograma))

    print ('Mensagem Original: {}'.format( mensagem))

def affine_cifra(mensagem, chave):
    return ''.join([ chr(((chave[0]*(ord(t) - ord('A')) + chave[1] ) % 26)
                         + ord('A')) for t in mensagem.upper().replace(' ', '')])

main()
