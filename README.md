***Criptografia e Criptanalise Aplicadas - Criptanalise***


Exercicios em Python


# Reference:

- book - > https://inventwithpython.com/hacking/


# Criptoanálise
crip·to·a·ná·li·se\
(cripto- + análise)\
nome feminino\
Análise ou decifração de comunicação ou escrita codificada ou secreta. = CRIPTANÁLISE

***Palavras relacionadas:*** criptanálise, criptologia, criptoanalista, criptoanalítico.

1. O que entende por criptanalise?

***Descrição:*** 
Criptoanálise é um processo de encontrar pontos fracos em algoritmos criptográficos e usar essas fraquezas para decifrar o texto cifrado sem conhecer a chave secreta (exemplo dedução). Às vezes não é a fraqueza no próprio algoritmo criptográfico, mas sim na forma como é aplicada que faz criptoanálisis bem sucedidas. Um atacante pode ter outros objetivos, bem como, tais como:

2. Argumente sobre ataques por criptanalise.

- Total Break - Encontrar a chave secreta.

- Dedução Global - Encontrar um algoritmo funcionalmente equivalente para criptografia e descriptografia que não requer o conhecimento da chave secreta.

- Informações Dedução - Ganhando algumas informações sobre textos planos ou mensagens cifradas que não eram conhecidas anteriormente.

- Algoritmo Distinguido - O atacante tem a capacidade de distinguir a saída da encriptação (encriptado) a partir de uma permutação aleatória de bits.

O objetivo do atacante realizar criptoanálise vai depender das necessidades específicas do atacante em um determinado contexto ataque. Na maioria dos casos, se a criptoanálise é bem sucedida em tudo, um atacante não vai ser capaz de ir além de ser capaz de deduzir algumas informações sobre o texto simples (meta 3). No entanto, isto pode ser suficiente para um atacante, dependendo do contexto.

***Exemplos***

Um exemplo muito fácil de entender (mas totalmente inaplicável às modernas cifras criptográficas) é uma técnica de criptoanálise chamada análise de frequência que pode ser aplicada com sucesso para os algoritmos de criptografia clássicos básicos que realizaram substituição monoalfabética substituindo cada letra do texto com sua carta de mapeamento predeterminado do mesmo alfabeto. Isso foi considerado um avanço em relação a técnica mais básica que simplesmente muda todas as letras do texto original por um número constante de posições e substitui as letras originais com a nova carta como a posição do alfabeto resultante. Embora as cifras de substituição monoalfabética sejam resistentes à força bruta cega, eles podem ser facilmente quebrados com nada mais do que uma caneta e papel. Análise criptoanálise de freqüência usa o fato de que a linguagem natural não é aleatória e a substituição monoalfabética não esconde as propriedades estatísticas da linguagem natural. Então, se a letra "E" em uma linguagem portuguesa ocorre com uma certa freqüência conhecida (cerca de 12,7%), seja qual for "E" foi substituído por chegar ao texto cifrado, irá ocorrer com a freqüência similar. Tendo esta informação de freqüência permite que o criptoanalista para determinar rapidamente as substituições e decifrar o texto cifrado. Técnicas de análise de frequência não são aplicáveis a cifras modernas, todas elas são resistentes a ele (a não ser que este é um caso grave de um algoritmo de criptografia caseiros). Este exemplo é apenas para ilustrar um exemplo rudimentar de criptoanálise.
