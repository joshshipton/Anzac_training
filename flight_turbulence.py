n = [int(item) for item in input().split()]
people = [int(item) for item in input().split()]
count = 0
wannaMove = n[1]
first = True

while True:
    # get the index of the person who wants to move
    index = people.index(wannaMove)
    #check that they arent already in the right spot
    if index != wannaMove - 1:
        # check what is currently where they are meant to be 
        inTheWay = people[wannaMove-1]
        if first:
            count +=2
            first = False
        else:
            count += 1

        if inTheWay == index + 1:
            break
    else:
        break
    if index == people[wannaMove-1]:
        break
    if count == len(people):
        break

print(count)

#solved 