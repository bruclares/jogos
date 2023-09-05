def jogar():

    print("***********************************")
    print("****Bem vindo ao jogo de Forca!****")
    print("***********************************")

    palavra_secreta = "banana".upper()
    letras_acertadas = ["_" for letra in palavra_secreta] # List Comprehension (compreensão de lista) aqui vai criar a lista de "_" no tamanmho da palavra secreta, que vai poder mudar dinamicamente
    letras_faltando = str(letras_acertadas.count("_"))
    enforcou = False
    acertou = False
    erros = 0

    print(letras_acertadas)
    print("Ainda faltam acertar {} letras".format(letras_faltando))

    # enquanto não enforcou e não acertou (enquanto true)
    while (not enforcou and not acertou):
        chute = input("Qual a letra? ")
        chute = chute.strip().upper() #retira os espaços da entrada
        index = 0  # posição

        if (chute in palavra_secreta):
            for letra in palavra_secreta:
                if (chute == letra): # função vai tornar as letras maisculas e comparar
                    letras_acertadas[index] = letra
                index = index + 1
            
        else:
            erros = erros + 1
            print("Ops, você errou! Faltam {} tentivas.".format(6 - erros))
        
        enforcou = erros == 6
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)
    
    if (acertou):
        print("Você Ganhou! ")
    else:
        print("Você perdeu! ")
    print("Fim do jogo!")


if (__name__ == "__main__"):
    jogar()
