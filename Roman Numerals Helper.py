class RomanNumerals:

    def from_roman(roman_num):
        table = {'M' : 1000, 'CM' : 900, 'D' : 500, 'CD' : 400, 'C' : 100, 'XC' : 90, 'L' : 50, 'XL' : 40, 'X' : 10, 'IX' : 9, 'V' : 5, 'IV' : 4, 'I' : 1}
        result = 0
        i = 0
        while i < len(roman_num):
            if i + 1 < len(roman_num) and table.get(roman_num[i:i+2]) != None:
                result += table.get(roman_num[i:i+2])
                i += 2
            elif table.get(roman_num[i]) != None:
                result += table.get(roman_num[i])
                i += 1
        return result
            
            
    def to_roman(val):
        table = [(1000, "M"),(900, "CM"),(500, "D"),(400, "CD"),(100, "C"),(90, "XC"),(50, "L"),(40, "XL"),(10, "X"),(9, "IX"),(5, "V"),(4, "IV"),(1, "I")]
        result = ''
        for cap, roman in table:
            divident, remainder = divmod(val, cap)
            result += roman * divident
            val = remainder
        return result