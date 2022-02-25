class Solution:
    def romanToInt(self, s: str) -> int:
        roman_sum = 0
        roman_constant_data = ["IV", "IX", "XL", "XC", "CD", "CM"]
        roman_dic = {
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000
        }
        add = 0
        for n in roman_constant_data:
            if n in s:
                roman_sum = roman_sum + (roman_dic[n[1]]-roman_dic[n[0]])   
                print(roman_sum)
                s = s.replace(n, "")
        for n in s:
            roman_sum = roman_sum + roman_dic[n]

        return roman_sum