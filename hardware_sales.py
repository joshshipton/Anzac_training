n = [int(item) for item in input().split()]

ids = []
temp_dick = {}

store1 = [int(item) for item in input().split()]
for i in range(1, len(store1), 2):
    if store1[i-1] not in temp_dick:
        temp_dick[store1[i-1]] = store1[i]
    else:
         temp_dick[store1[i-1]] += store1[i]
    for item in temp_dick:
        if temp_dick[item] >= 20:
            ids.append(temp_dick[item])

print(temp_dick)

temp_dick = {}

store2= [int(item) for item in input().split()]
for i in range(1, len(store2), 2):
    temp_dick[store2[i-1]] = store2[i]
    for item in temp_dick:
        if temp_dick[item] >= 20:
            ids.append(temp_dick[item])
temp_dick = {}
store1 = [int(item) for item in input().split()]
for i in range(1, len(store1), 2):
    temp_dick[store1[i-1]] = store1[i]
    for item in temp_dick:
        if temp_dick[item] >= 20:
            ids.append(temp_dick[item])



print(ids)
dick = {}
final = []

for item in ids:
    if item in dick:
        dick[item] += 1
    else:
        dick[item] = 1


for item in dick:
    if dick[item] >= 3:
        final.append(dick[item])


print(len(final), end=' ')
for item in final:
    print(item, end=' ')
