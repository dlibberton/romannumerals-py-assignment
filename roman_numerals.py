def to_roman(num):
    #print(type(num))
    if type(num) != int or num <= 0:
        return 'error'
    ROMAN_NUMERAL_TO_ARABIC_MAP = {
        "M": 1000,
        "CM": 900,
        "D": 500,
        "CD": 400,
        "C": 100,
        "L": 50,
        "XL": 40,
        "X": 10,
        "IX": 9,
        "V": 5,
        "IV": 4,
        "I": 1,
    }
    output = ""
    while num > 0:
        for x in ROMAN_NUMERAL_TO_ARABIC_MAP:
            if num / ROMAN_NUMERAL_TO_ARABIC_MAP[x] >= 1:
                output += x
                num -= ROMAN_NUMERAL_TO_ARABIC_MAP[x]

    return output

to_roman(70)