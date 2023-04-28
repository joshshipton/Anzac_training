n = input()
ids = []

def checkdick(n):
    for key, value in n.items():
        if value >= 20:
            ids.append(key) 
    
def makedick(storedict):
    storenum = input().split()
    for i in range(0, len(storenum), 2):
        if storenum[i] in storedict:
            storedict[storenum[i]] += int(storenum[i+1])
        else:
            storedict[storenum[i]] = int(storenum[i+1])
            

store1dict = {}
makedick(store1dict)
checkdick(store1dict)

store2dict = {}
makedick(store2dict)
checkdick(store2dict)


store3dict = {}
makedick(store3dict)
checkdick(store3dict)

final = {}

for id in ids:
    if id in final:
        final[id] += 1
    else:
        final[id] = 1

print(final)
last = []

for key, value in final.items():
    if value == 3:
        last.append(key)


print(len(last), end=' ')
for item in last:
    print(item, end= ' ')