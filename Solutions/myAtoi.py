# NAME : String to Integer (atoi)
# LINK : https://leetcode.com/problems/string-to-integer-atoi/
# DATE : 01/02/2021


class Solution:
    def myAtoi(self, s: str) -> int:
        k = len(s)
        result = 0
        sign = True
        a = True
        b = True

        for i in range(k):
            if ord(s[i]) > 47 and ord(s[i]) < 58:
                result = result * 10 + (ord(s[i]) - 48)
                b = False
                continue
            if not b or not a:
                break

            if s[i] == " ":
                continue

            if s[i] == "+" or s[i] == "-":
                sign = s[i] == "+"
                a = False
                continue

            if result > 0:
                break

            return 0

        result *= 1 if sign else -1
        if result < -2147483648:
            return -2147483648
        elif result > 2147483647:
            return 2147483647
        else:
            return result
