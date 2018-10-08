#!/usr/bin/python3
from forca import *

iword = int(input("Escolha um numero entre 0 e 49: "))

if iword > 49:
    print("Numero invalido.")
else:
    print("")
    i = 0
    wrong = []
    win = False
    word = lista_palavras[iword]

    vword = []
    rigth = []
    total = []
    for c in word:
        vword.append(c)
        rigth.append(0)

    while not win and i < len(cenas_forca) -1:
        show = ""
        for c in range(len(rigth)):
            if rigth[c] == 1:
                show+=vword[c]
            else:
                show+="_"
            if c < len(rigth) -1:
                show +="  "

        print(cenas_forca[i])

        print("Palavra:", show)
        
        if len(wrong) > 0:
            print("Tentativa(s) incorreta(s): ", end="")
            for c in range(len(wrong)):
                if c < len(wrong) -1:
                    print(wrong[c],end=" ")
                else:
                    print(wrong[c])

        char = input("Proxima letra: ")

        if char in total:
            print("Voce jah escolheu esta letra.")

        elif char in vword:
            for c in range(len(vword)):
                if char == vword[c]:
                    rigth[c] = 1
        else:
            wrong.append(char)
            i+=1
        print("")

        total.append(char)

        if 0 not in rigth:
            win = True

            show = ""
            for c in range(len(rigth)):
                if rigth[c] == 1:
                    show+=vword[c]
                else:
                    show+="_"
                if c < len(rigth) -1:
                    show +="  "

            print(cenas_forca[i])

            print("Palavra:", show)
            
            if len(wrong) > 0:
                print("Tentativa(s) incorreta(s): ", end="")
                for c in range(len(wrong)):
                    if c < len(wrong) -1:
                        print(wrong[c],end=" ")
                    else:
                        print(wrong[c])
            

    if win:
        print("Palavra encontrada!")

    else:
        show = ""
        for c in range(len(rigth)):
            if rigth[c] == 1:
                show+=vword[c]
            else:
                show+="_"
            if c < len(rigth) -1:
                show +="  "

        print(cenas_forca[i])

        print("Palavra:", show)
        
        if len(wrong) > 0:
            print("Tentativa(s) incorreta(s): ", end="")
            for c in range(len(wrong)):
                if c < len(wrong) -1:
                    print(wrong[c],end=" ")
                else:
                    print(wrong[c])

        print("Palavra oculta:", word)
