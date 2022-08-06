def jogar():

    apresentacao()
    palavra = palavra_sec()
    lista = ["_" for x in palavra]
    erros = 0
    tentativas = 7
    enforcou = False
    acertou = False


    print(lista)
    print("----------------------")
    print("Você tem {} tentativas".format(tentativas))
    print("----------------------")



    while not acertou and not enforcou:
        chutes = chutando()
        if chutes in palavra:
            acertando(palavra, chutes, lista)
            print("-------------")
            print("Você acertou!")
            print("-------------")
            print(lista)
            print("------------------")

        else:
            if erros == 6:
                enforcou is True
                enforcado(palavra)
                break
            else:
                erros += 1
                tentativas = (erros - 7) * (-1)
                print("-----------------")
                print("Puxa, você errou!")
                print("-----------------")
                print("Você ainda tem {} tentativas".format(tentativas))
                print("  _______     ")
                print(" |/      |    ")
                msg_perdendo(erros)
                continue

        if "_" not in lista:
            acertou is True
            vencedor()
            break



def apresentacao():
    print("--------------------------")
    print("Bem-vindo ao jogo da forca")
    print("--------------------------")

def palavra_sec():
    arquivo = open("words.txt", "r")
    pala_sec = []
    for x in arquivo:
        pala_sec.append(x.strip())
    arquivo.close()
    import random
    palavra = pala_sec[random.randrange(0, (len(pala_sec)))].upper()
    return palavra

def chutando():

    chute = input("Escolha uma letra: ")
    chute = chute.strip().upper()
    return chute

def acertando(palavra, chutes, lista):
    index = 0
    for letra in palavra:
        if chutes == letra:
            lista[index] = chutes
        index += 1
    return lista

def msg_perdendo(erros):
    if (erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if (erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if (erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if (erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if (erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if (erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")




def enforcado(palavra):

    print("  _______     ")
    print(" |/      |    ")
    print(" |      (_)   ")
    print(" |      \|/   ")
    print(" |       |    ")
    print(" |      / \   ")
    print(" |            ")
    print("_|___         ")
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra))
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

def vencedor():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

jogar()
