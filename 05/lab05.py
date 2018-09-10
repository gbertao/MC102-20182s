n = int(input())
lines = []
resp = []

for i in range(0, n):
    lines.append(input())

h = 0
e = 0
for i in range(0,n):
    if not (lines[i].isalpha() or lines[i].isdigit()) :
        if lines[i][0] == '#' and lines[i][1:].isalpha():
            h+=1
        elif not (lines[i][1:].isdigit() and lines[i][0] in ("-","+")):
            e+=1
        else:
            resp.append(lines[i])
    else:
        resp.append(lines[i])

for i in resp:
    print(i)

if h > 0:
    if h == 1:
        print("1 hashtag foi removida.")
    else:
        print(h, "hashtags foram removidas.")

if e > 0:
    if e == 1:
        print("1 emoticon foi removido.")
    else:
        print(e, "emoticons foram removidos.")
