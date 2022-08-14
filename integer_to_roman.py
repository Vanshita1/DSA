#Given an integer, convert it to a roman numeral.



class Solution:
    def intToRoman(self, num: int) -> str:
        roman_int = {1:'I',4:'IV', 5:'V', 9:'IX', 10:'X', 40:'XL', 50:'L', 90: 'XC', 100:'C', 400: 'CD', 500:'D', 900: 'CM', 1000:'M'}
        roman = ""
        values = list(roman_int.keys())
        values.reverse()
        
        while num:
            for value in values:
                q = num/value
                if q >= 1:
                    roman += roman_int[value]
                    num -= value
                    break
        return roman

#solution 2

class Solution:
    def intToRoman(self, num: int) -> str:
        roman_int = [["I", 1], ["IV", 4], ["V", 5], ["IX", 9], ["X", 10], ["XL", 40], ["L", 50], ["XC", 90], ["C", 100],   ["CD", 400], ["D", 500], ["CM", 900], ["M", 1000]]
        roman = ""
        for rom, val in reversed(roman_int): 
            if num//val:
                count = num//val
                roman += (rom*count)
                num = num%val
        return roman


        

