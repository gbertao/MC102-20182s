n1 = float(input())
n2 = float(input())
n3 = float(input())

FM = input()
Fm = input()

DTM = int(input())
DTm = int(input())

hotel = float(input())
passagem = float(input())

if n1 < 7 or n2 < 7 or n3 < 7:
    print("NAO. As notas da Carla nao foram suficientes.")

elif FM == "Nao" or Fm == "Nao":
    print("NAO. O casal nao esta de ferias.")

elif DTM >= 11 and DTm >= 11:
    print("NAO. Nenhum 13o salario foi liberado a tempo.")

elif hotel + passagem > 10000:
    print("NAO. O valor total e muito alto.")

else:
    print("SIM!!!")
