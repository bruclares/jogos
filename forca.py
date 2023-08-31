def jogar():

    print("***********************************")
    print("****Bem vindo ao jogo de Forca!****")
    print("***********************************")

    palavra_secreta = "banana"
    letras_acertadas = ["_","_","_","_","_","_"]
    letras_faltando = str(letras_acertadas.count("_"))
    enforcou = False
    acertou = False

    print(letras_acertadas)
    print("Ainda faltam acertar {} letras".format(letras_faltando))

    # enquanto não enforcou e não acertou (enquanto true)
    while (not enforcou and not acertou):
        chute = input("Qual a letra? ")
        chute = chute.strip() #retira os espaços da entrada
        index = 0  # posição

        for letra in palavra_secreta:
            if (chute.upper() == letra.upper()): # função vai tornar as letras maisculas e comparar
                letras_acertadas[index] = letra
            index = index + 1     
        print(letras_acertadas)

    print("Fim do jogo!")


if (__name__ == "__main__"):
    jogar()
