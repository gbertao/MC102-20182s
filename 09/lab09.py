chart = []

values = {'B':0, 'I':1, 'N':2, 'G':3, 'O':4}

for i in range(5):
    chart.append([])

for j in range(5):
    b, i, n, g, o = input().split()

    chart[j].append(b)
    chart[j].append(i)
    chart[j].append(n)
    chart[j].append(g)
    chart[j].append(o)

n = int(input())

print("+----------------+\n| B  I  N  G  O  |\n+================+")
for j in range(5):
    print("|", end=" ")
    for k in range(5):
        print(chart[j][k], end=" ")
    print("|")
print("+----------------+")

bingo = False
while n > 0:
    char, num = input().split("-")
    achou = False

    for j in range(5):
        if num == chart[j][values[char]]:
            achou = True
            chart[j][values[char]] = "XX"

    print(char+"-"+num)

    if achou:
        print("+----------------+\n| B  I  N  G  O  |\n+================+")
        for j in range(5):
            print("|", end=" ")
            for k in range(5):
                print(chart[j][k], end=" ")
            print("|")
        print("+----------------+")

    # Horizontal
    for j in range(5):
        total = 0
        for k in range(5):
            if chart[j][k] == "XX":
                total+=1

        if total >= 5:
            n = 0
            bingo = True
            break

    # Vertical
    for j in range(5):
        total = 0
        for k in range(5):
            if chart[k][j] == "XX":
                total+=1

        if total >= 5:
            n = 0
            bingo = True
            break

    # Diag princ
    total = 0
    for i in range(5):
        if chart[i][i] == "XX":
            total += 1

    if total >=5:
        n = 0
        bingo = True
        break
        
    # Diag sec
    total = 0
    for i in range(5):
        if chart[i][4-i] == "XX":
            total += 1

    if total >=5:
        n = 0
        bingo = True
        break
    n-=1

if bingo:
    print("BINGO!")
