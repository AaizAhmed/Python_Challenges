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

def permute(prefix, permStr):

    length = len(permStr)

    if length == 0:
        print(prefix)
    else:
        for index in range(length):
            permute(prefix+permStr[index], permStr[0:index]+permStr[index+1:length])


def permute_2(permStr, first, last):

    if first == last:
        print(permStr)
    else:
        for index in range(first, last, +1):
            permStr = swap(permStr, first, index)
            permute_2(permStr, first+1, last)
            permStr = swap(permStr, first, index)

def swap(permStr, first, last):

    charStr = list(permStr)

    tmp = charStr[first]
    charStr[first] = charStr[last]
    charStr[last] = tmp

    return ''.join(charStr)

permute_2('abc', 0, 3)
myStr = 'abc'


