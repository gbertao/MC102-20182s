num = input().zfill(3)
vet = input().split()

for i in range(len(vet)):
    vet[i] = vet[i].zfill(3)

def printar(vet, i, f, meio):
    for j in range(len(vet)):
        if j>=f:
            break
        if j == meio:
            print("+=====", end="")
        elif j < i or j >= f:
            print(" "*6, end="")
        else:
            print("+-----", end="")
    print("+")

    for j in range(len(vet)):
        if j>=f:
            break
        if j == meio:
            print("||"+vet[j]+"|",end="")
        elif j < i or j >= f:
            print(" "*6, end="")
        else:
            print("|",vet[j],end=" ")
    print("|")

    for j in range(len(vet)):
        if j>=f:
            break
        if j == meio:
            print("+=====", end="")
        elif j < i or j >= f:
            print(" "*6, end="")
        else:
            print("+-----", end="")
    print("+")
        
def BB(vet, x, i, f):
    if i < f:
        meio = (i+f-1)//2
        printar(vet,i,f, meio)
        if x < vet[meio]:
            BB(vet, x, i, meio)
        elif x > vet[meio]:
            BB(vet, x, meio+1, f) 
        else:
            print("O elemento estah na posicao", meio)
    else:
        print("O elemento nao foi encontrado")

def check(vet):
    for i in range(0, len(vet) -1):
        if vet[i] > vet[i+1]:
            return False
    return True

print("Elemento procurado:", num)
printar(vet, 0, len(vet), -1)
if check(vet):
    BB(vet, num, 0, len(vet))
else:
    print("Vetor nao estah ordenado")
