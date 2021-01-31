# NAME : Integer to Roman
# LINK : https://leetcode.com/problems/integer-to-roman/
# DATE : 31/01/2021


class Solution:
    def intToRoman(self, num: int) -> str:
        roman = [
            [1000, "M"],
            [900, "CM"],
            [500, "D"],
            [400, "CD"],
            [100, "C"],
            [90, "XC"],
            [50, "L"],
            [40, "XL"],
            [10, "X"],
            [9, "IX"],
            [5, "V"],
            [4, "IV"],
            [1, "I"],
        ]
        k = 13
        result = ""
        toPop = 0
        while num > 0:
            for i in range(k):
                if num >= roman[i][0]:
                    num -= roman[i][0]
                    result += roman[i][1]
                    break
                else:
                    toPop += 1
            while toPop > 0:
                roman.pop(0)
                k -= 1
                toPop -= 1
        return result
