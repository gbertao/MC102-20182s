ga = 0
sa = 0
ba = 0

gold = float(input())
silver = float(input())
bronze = float(input())

nota = float(input())

maior = nota

while nota != -1:
    
    if nota >= gold:
        ga+=1
    elif nota >= silver:
        sa+=1
    elif nota >= bronze:
        ba+=1

    if nota > maior:
        maior = nota

    nota = float(input())

if ga > 0:
    print ("Medalha(s) de ouro:", ga)
else:
    print("Nenhum participante recebeu medalha de ouro!")

if sa > 0:
    print ("Medalha(s) de prata:", sa)
else:
    print("Nenhum participante recebeu medalha de prata!")

if ba > 0:
    print ("Medalha(s) de bronze:", ba)
else:
    print("Nenhum participante recebeu medalha de bronze!")

print("Maior nota: {:.1f}".format(maior))
