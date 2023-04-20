# The Goldbach Conjecture states that any even number greater than 3 can be expressed as the sum of two primes
# (primes are numbers that have exactly two factors: themselves and 1). It has never been proven for all even
# numbers, but it has been demonstrated to be true for all of the numbers that we’ll use for this problem. Consider
# any even integer x > 3. There may be many pairs of primes which sum to x. Take the pair with the largest
# difference. That difference must be even, and less than x. So, repeat the trick. How many steps does it take until
# you reach an even number less than 3 (2 or 0)?
# Input
# Each input will consist of a single test case. Note that your program may be run multiple times on different inputs.
# Each test case will consist of a single line with a single integer x (0 ≤ x ≤ 106, x is even).
# Output a single integer, which is the count of Repeating Goldbach steps until the number is less than 3.

n = int(input())

def getPrimes(n):
    primes = []
    for i in range(2, n+1):
        is_prime = True
        for j in range(2, int(i**0.5)+1):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(i)
    return primes

            

def findBigDiff(n, steps=1):
    # here we want to point from the front and back of the list and return the first that add up to n
    primes = getPrimes(n)
    print('primes numbers are: ', end='')
    print(primes)
    sthap = False
    for i in range(len(primes)):
        #  need to change how this works, for each num start at the back and loop thru
        for j in range(len(primes)-i):
             if primes[i] + primes[-j-1] == n:
                difference =  abs(primes[i] - primes[-j-1])
                print("the primes with the bigg diff are: ",primes[i] ,"+", primes[-i-1], 'the difference is: ', difference)
                sthap = True
                break
        if sthap:
            break

    # keep calling difference until its less than 3 
    if difference < 3:
        print(steps)
    else:
        steps += 1
        findBigDiff(difference, steps)
        

findBigDiff(n)

# time error for 999982