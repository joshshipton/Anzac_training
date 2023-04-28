# Fastest way of generating a list of prime numbers in python

def sieve(n):
    prime = [True for _ in range(n+1)]
    prime[0], prime[1] = False, False
    for i in range(2, int(n**0.5)+1):
        for j in range(2*i, n+1, i):
            prime[j] = False
    return prime


n = int(input('Enter a number: '))

list = sieve(n)

print('Your primes are: ', end="")

for i in range(n+1):
    if list[i]:
        print(i, end=" ")
