#Roman Numerals Helper
#https://www.codewars.com/kata/51b66044bce5799a7f000003/train/python

roms = ["M", "D", "C", "L", "X", "V", "I"]
nums = [1000, 500, 100, 50, 10, 5, 1]

illegal_roms = ["DCCCC", "CCCC", "LXXXX", "XXXX", "VIIII", "IIII"]
legal_roms = ["CM", "CD", "XC", "XL", "IX", "IV"]

def to_roman(n):
    am = n
    res = ''

    #Decrease the number with the largest roman letter first
    for i in range(len(nums)):
        while am - nums[i] >= 0:
            am -= nums[i]
            res += roms[i]

    #Convert illegal romans with the proper one
    for i in range(len(illegal_roms)):
        if illegal_roms[i] in res:
            res = res.replace(illegal_roms[i], legal_roms[i])

    return res

def from_roman(roman_num):
    res = 0
    prev_num = ""

    for letter in roman_num:
        number = nums[roms.index(letter)]
        if prev_num == "": #First letter
            prev_num = number
            res += number
        elif prev_num < number:
            res += number - 2*prev_num #Solution for case like "IX", "IV", etc.
        else:
            res += number #Simply translate the latter
            prev_num = number 

    return res

print(from_roman("MCDXCIV"))
print(to_roman(1494))