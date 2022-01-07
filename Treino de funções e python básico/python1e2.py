from random import randrange, choice


def abertura():
    print("************************************************")
    print("***************BEM VINDO AO JOGO****************")
    print("************************************************")


def palavra_secreta(nomedoarquivo):
    # abertura do arquivo que tera as palavras aleatorias
    arquivo = open(nomedoarquivo, "r")
    # retorna uma linha aleatoria e parte ela pelos espaços
    palavra_secreta = choice(arquivo.readline().split())
    arquivo.close()
    return palavra_secreta


def checagemcorreto(chute, palavra, word):
    erros = 0
    if chute in palavra:
        index = 0
        for i in palavra:
            if i == chute:
                print("encontrei a letra {} na posição {}".format(chute, index))
                word[index] = chute

            index += 1


def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if erros == 1:
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if erros == 2:
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if erros == 3:
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if erros == 4:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if erros == 5:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if erros == 6:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if erros == 7:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")


def imprime_mensagem_vencedor():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")


def imprime_mensagem_perdedor(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")


def fim(venceu, enforcou):
    if venceu:
        imprime_mensagem_vencedor()
    else:
        imprime_mensagem_perdedor()
    print("fim do jogo")


def advinhacao():
    abertura()
    numero_secreto = randrange(0, 101)
    tentativas = 3

    for rodadas in range(1, 1 + tentativas):
        print("tentativa:", rodadas, " de ", tentativas)
        z = int(input('digite o valor'))

        if z == numero_secreto:
            print("voce ganhou ")
            break
        elif z < numero_secreto:
            print("voce falhou, seu numero esta muito baixo")

        elif z > numero_secreto:
            print("voce falhou, seu numero esta muito alto")


# jogo da forca para treinar manutenção de string
def forca():

    abertura()
    palavra = palavra_secreta("palavras")
    word = ['_'] * len(palavra)

    erros = 0
    enforcou = False
    venceu = False

    print(word)
    # condição de quebra do loop
    while not enforcou and not venceu:

        print("jogando...")
        chute = str(input("Qual a letra??"))
        chute = chute.lower().strip()
        # condição que checa se a letra esta na palavra secreta
        if chute in palavra:
            checagemcorreto(chute, palavra, word)

        else:
            erros += 1
            desenha_forca(erros)

        enforcou = erros == 7
        venceu = "_" not in word

        print(word)

    fim(venceu, enforcou)
