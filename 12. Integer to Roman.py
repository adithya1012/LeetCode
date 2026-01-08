class Solution:
    def intToRoman(self, num: int) -> str:
        mapper = [
            (1, "I"),
            (4, "IV"),
            (5, "V"),
            (9, "IX"),
            (10, "X"),
            (40, "XL"),
            (50, "L"),
            (90, "XC"),
            (100, "C"),
            (400, "CD"),
            (500, "D"),
            (900, "CM"),
            (1000, "M")
        ]
        res = ""
        for val, sym in mapper[::-1]:
            i = num // val
            if i:
                num = num % val
                res += sym * i
        return res

print(Solution().intToRoman(4000))