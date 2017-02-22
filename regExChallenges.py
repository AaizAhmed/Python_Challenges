
def convertToRoman (decimal):

    # Making a string that has "I" decimal number of times.
    roman = "I" * decimal

    roman = roman.replace('IIIII', 'V').replace('IIII', 'IV').replace('VV', 'X') \
                 .replace('VIV', 'IX').replace('XXXXX', 'L').replace('XXXX', 'XL') \
                 .replace('LL', 'C').replace('LXL', 'XC').replace('CCCCC', 'D') \
                 .replace('CCCC', 'CD').replace('DD', 'M').replace('DCD', 'CM')

    return roman

def convertToDecimal (roman):

    roman = roman.upper()

    roman = roman.replace("CM", "DCD").replace("M", "DD").replace("CD", "CCCC") \
                 .replace("D", "CCCCC").replace("XC", "LXL").replace("C", "LL") \
                 .replace("XL", "XXXX").replace("L", "XXXXX").replace("IX", "VIV") \
                 .replace("X", "VV").replace("IV", "IIII").replace("V", "IIIII")

    return len( roman )

# print( convertToRoman(3999) )
# print( convertToDecimal("mmmcmxcix") )

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

print( fibonacci(10) )
