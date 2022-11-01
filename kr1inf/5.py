def Unification(dict1, dict2):
    return {**dict1, **dict2}


a = Unification({1: 5, 2: 7}, {3: 6})
print(a)
