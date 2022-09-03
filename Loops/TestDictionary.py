testDict = {'t1': 10, 't2': 12, 't3': 15}

for key in testDict:
    print(key)

for key in testDict.items():
    print(key)

for key, value in testDict.items():
    print(key, value)
