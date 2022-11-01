s = input().split()
d = {}
for i in s:
    i = i.strip('.,').lower()
    d[i] = d.get(i, 0) + 1
print(min(d.items(), key=lambda x: (x[1], x[0],))[0])