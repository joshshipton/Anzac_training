n = [int(item) for item in input().split()]
people = [int(item) for item in input().split()]
count = 0
wannaMove = n[1]

def checkPlace(people, wannaMove, count):
    index = people.index(wannaMove)
    print(index,wannaMove)
    if index != wannaMove - 1:
        print(index, wannaMove)
        wannaMove = people[wannaMove-1]
        count += 1 
        checkPlace(people, wannaMove, count)
    else:

        return count

checkPlace(people, wannaMove, count)
print(count)

#  not solved 