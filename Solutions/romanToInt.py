# NAME : Roman to Integer
# LINK : https://leetcode.com/problems/roman-to-integer/
# DATE : 29/01/2021, 20/02/2021


class Solution:
    def romanToInt(self, s: str) -> int:
        lookup = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        result = 0
        current_max = 1

        for i in range(0, len(s)):
            n = lookup[s[-(i + 1)]]
            if n >= current_max:
                current_max = n
                result += n
            else:
                result -= n

        return result


class Solution2:
    def romanToInt(self, s: str) -> int:
        romans = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        result = 0
        maxSeen = s[-1]
        for i in range(1, len(s) + 1):
            if romans[s[-i]] >= romans[maxSeen]:
                result += romans[s[-i]]
                maxSeen = s[-i]
            else:
                result -= romans[s[-i]]
        return result
