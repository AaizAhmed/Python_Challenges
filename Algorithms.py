import math

def isPrime(num):

    if num < 2:
        return False

    sqrtNum =   int( math.sqrt(num) )
    for divideBy in range(2, sqrtNum+1, +1):
        if num % divideBy == 0:
            return False

    return True

def nextPrime(num):

    index = num
    while True:

        if isPrime(index):
            return index

        index += 1

def primeFactors(num):

    factors = []

    for index in range(2, num, +1):
        if isPrime(index):
            if num % index == 0:
                factors.append(index)

    return factors

def nthFib(num):

    first = 0
    second = 1
    nextNum = 0

    if num == 1:
        return first
    if num == 2:
        return second

    for count in range(3, num+1, +1):
        nextNum = first + second
        first = second
        second = nextNum

    return nextNum

print( nthFib(2) )
print( nthFib(3) )
print( nthFib(5) )
print( nthFib(8) )


