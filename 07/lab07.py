def tupla_float_int(x) :
    x = x[1:-1]       # remove parênteses
    x = x.split(",")  # separa em duas strings
    f = float(x[0])   # converte primeiro elemento para float
    i = int(x[1])     # converte segundo elemento para int
    return (f,i)      # retorna tupla

notas_c = input().split()
notas_lab = [tupla_float_int(x) for x in input().split()]
p1,p2 = [float(x) for x in input().split()]
freq = float(input())

mediac = 0

for i in notas_c:
    mediac += float(i)

mediac = mediac/len(notas_c)

medial = 0
pesot = 0
for nota,peso in notas_lab:
    medial += peso * nota 
    pesot += peso

medial = medial / pesot

mediap = (2*float(p1) + 3*float(p2))/5

print("Media das atividades conceituais:", format(mediac,".1f"))
print("Media das tarefas de laboratorio:", format(medial,".1f"))
print("Media das provas:", format(mediap,".1f"))

if freq > 75:
    if mediap >= 5 and medial >= 5:
        Melem = 0.6*mediap+0.3*medial+0.1*mediac
        print("Aprovado(a) por nota e frequencia.")
        print("Media final:", format(max(5,Melem), ".1f"))

    elif mediap < 2.5 or medial < 2.5:
        print("Reprovado(a) por nota.")
        print("Media final:",format(min(mediap,medial), ".1f"))

    else:
        exame = float(input())
        mf = (min(mediap, medial) + exame) / 2
        print("Nota no exame:", exame)
        if mf >= 5:        
            print("Aprovado(a) por nota e frequencia.")
            print("Media final:", format(mf, ".1f"))
        else:
            print("Reprovado(a) por nota.")
            print("Media final:", format(mf, ".1f"))
else:
    print("Reprovado(a) por frequencia.")
    print("Media final:", format(min(mediap,medial), ".1f"))
