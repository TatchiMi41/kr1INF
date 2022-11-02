def Unification(*dict_name: dict):
    c = {}
    for i in dict_name:
        for key, value in i.items():
            if key not in c.keys():
                c.update({key: []})
            if isinstance(value, list):
                c[key] += value
            else:
                c[key] += [value]
    return c


a = {1: 'adfhjagsl', 2: 'afdhnr'}
b = {2: 'pdofofofof', 3: 'iiowjgt[p'}
c = {4: 'jjfosijog'}
print(Unification(a, b, c))
