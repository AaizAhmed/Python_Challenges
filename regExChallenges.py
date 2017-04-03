
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

print( convertToRoman(3999) )
print( convertToDecimal("mmmcmxcix") )

