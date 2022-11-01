f = {}
for i in range(int(input())):
    n, operations = input().split()
    f[n] = operations
sm = [input().split() for i in range(int(input()))]
for j in sm:
    if f.get(j[1]) == j[0]:
        print('OK')
    else:
        print('Access denied')