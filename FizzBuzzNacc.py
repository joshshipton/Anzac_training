# Tmothy is interviewing at a big tech company called ICPC (International Cool Programming Corporation). He has been asked to program
# “FizzBuzz”. However, it is a variant of FizzBuzz that he has not seen on
# Stack Overflow before, and he is starting to panic. You must help him!
# In this version of FizzBuzz, an integer N is given. For this N, the
# FizzBuzz string contains exactly N parts, each of which is either fizz or
# buzz. The first part should be fizz if the number 1 is a Fibonacci number,
# or buzz otherwise. Likewise, the i-th part should be fizz if the number i
# is a Fibonacci number, or buzz otherwise. The first 8 Fibonacci numbers are 0, 1, 1, 2, 3, 5, 8, and 13 (all other
# Fibonacci numbers are larger than 13).
# Given N, find the FizzBuzz string

# get fib numbers up to the input 

def getFib(n):
    count = 0
    num1 = 1
    num2 = 1
    lst = [1]
    for i in range(n-1):
        count = num1+num2
        lst.append(count)

        num1 = num2
        num2  = count
    return lst 

def makestring(n):
    lst = getFib(n)

    for i in range(n):
        if i+1 in lst:
            print('fizz', end='')
        else:
            print("buzz", end='')
            

n = int(input(""))
makestring(n)


# solved
