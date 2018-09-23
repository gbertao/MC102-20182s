if not __debug__:
    import sys
    f = open(sys.argv[1])

def fat(n):
    if n < 1:
        return 1
    else:
        return n*fat(n-1)


if not __debug__:
    teams = int(f.readline())
else:
    teams = int(input())

matches = int(fat(teams)/fat(teams-2))

stats = {}

for i in range(matches):
    
    if not __debug__:
        match = f.readline()
    else:
        match = input()

    teamA, scoreA, lixo, teamB, scoreB = match.split()
    scoreA = int(scoreA)
    scoreB = int(scoreB)

    if not teamA in stats:
        stats[teamA] = {'GP':0, 'GC':0, 'W':0, 'P':0}
        
    stats[teamA]['GP']+=scoreA
    stats[teamA]['GC']+=scoreB

    if not teamB in stats:
        stats[teamB] = {'GP':0, 'GC':0, 'W':0, 'P':0}
        
    stats[teamB]['GP']+=scoreB
    stats[teamB]['GC']+=scoreA

    if scoreA > scoreB:
        stats[teamA]['W']+=1
        stats[teamA]['P']+=3

    elif scoreA == scoreB:
        stats[teamA]['P']+=1
        stats[teamB]['P']+=1

    else:
        stats[teamB]['W']+=1
        stats[teamB]['P']+=3

first = True
winner = None
for t in sorted(stats):
    if first:
        winner = t
        first = False

    else:
        if stats[winner]['P'] < stats[t]['P']:
            winner = t

        elif stats[winner]['P'] == stats[t]['P']:
            if stats[winner]['W'] < stats[t]['W']:
                winner = t

            elif stats[winner]['W'] == stats[t]['W']:
                SGw = stats[winner]['GP'] - stats[winner]['GC']
                SGt = stats[t]['GP'] - stats[t]['GC']
                if SGw < SGt:
                    winner = t

                elif SGw == SGt:
                    if stats[winner]['GP'] < stats[t]['GP']:
                        winner = t                

    print(t, stats[t]['P'], stats[t]['W'], stats[t]['GP'] - stats[t]['GC'], stats[t]['GP'])

print('Vencedor:', winner)

if not __debug__:
    f.close()
