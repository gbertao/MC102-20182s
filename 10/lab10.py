#!/usr/bin/python3
def printar(chart, m):
    for i in range(m-1):
        print("+----------------+",end=" ")
    print("+----------------+")
    for i in range(m-1):
        print("| B  I  N  G  O  |",end=" ")
    print("| B  I  N  G  O  |")
    for i in range(m-1):
        print("+================+",end=" ")
    print("+================+")

    for i in range(5):
        for j in range(m-1):
            print("|", end= " ")
            for k in range(5):
                print(chart[j][i][k], end=" ")
            print("|", end=" ")
                
        print("|", end=" ")
        for k in range(5):
            print(chart[m-1][i][k], end=" ")
        print("|")

    for i in range(m-1):
        print("+----------------+", end=" ")
    print("+----------------+")

def verifica(chart, char, num, m):
    achou = False
    for x in range(m):
        for j in range(5):
            if num == chart[x][j][values[char]]:
                achou = True
                chart[x][j][values[char]] = "XX"

    return achou
    
chart = []

values = {'B':0, 'I':1, 'N':2, 'G':3, 'O':4}

m = int(input())

for j in range(m):
    chart.append([])

    for i in range(5):
        chart[j].append([])

for k in range(m):
    for j in range(5):
        b, i, n, g, o = input().split()

        chart[k][j].append(b)
        chart[k][j].append(i)
        chart[k][j].append(n)
        chart[k][j].append(g)
        chart[k][j].append(o)

n = int(input())

printar(chart, m)

# Começo
bingo = False
while n > 0:
    char, num = input().split("-")
    achou = False

    achou = verifica(chart, char, num, m)


    print(char+"-"+num)

    if achou:
        printar(chart, m)

    for y in range(m):
        # Horizontal
        for j in range(5):
            total = 0
            for k in range(5):
                if chart[y][j][k] == "XX":
                    total+=1

            if total >= 5:
                n = 0
                bingo = True
                break

        if bingo:
            break

        # Vertical
        for j in range(5):
            total = 0
            for k in range(5):
                if chart[y][k][j] == "XX":
                    total+=1

            if total >= 5:
                n = 0
                bingo = True
                break

        if bingo:
            break

        # Diag princ
        total = 0
        for i in range(5):
            if chart[y][i][i] == "XX":
                total += 1

            if total >=5:
                n = 0
                bingo = True
                break

        if bingo:
            break
            
        # Diag sec
        total = 0
        for i in range(5):
            if chart[y][i][4-i] == "XX":
                total += 1

            if total >=5:
                n = 0
                bingo = True
                break
        if bingo:
            break
    n-=1

if bingo:
    print("BINGO!")
