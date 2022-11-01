s = [input().split() for i in range(int(input()))]
d = {}
for i in s:
    d[i[0]] = d.get(i[0], {})
    d[i[0]][i[1]] = d.get(i[0], {}).get(i[1], 0) + int(i[2])
for i in sorted(d):
    print(f'{i}:', sep='\n')
    for j in sorted(d[i]):
        print(f'{j} {d[i][j]}', sep='\n')