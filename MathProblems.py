
def fibonacci (number):

    if (number == 0):
        listFib = [0]
        return listFib
    elif (number == 1):
        listFib = [0, 1]
        return listFib
    else:
        listFib = [0, 1]

        for index in range(number - 1):

            first = listFib[ len(listFib) - 2]
            second = listFib[ len(listFib) - 1]
            listFib.append( first + second )

    return listFib

# print( fibonacci(10) )


board = [ 5*[0] for i in range(5) ]

board [3][3] = 4

print( board )
