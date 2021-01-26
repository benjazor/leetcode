# NAME : Reverse Integer
# LINK : https://leetcode.com/problems/reverse-integer/
# DATE : 26/01/2021


class Solution:
    def reverse(self, x: int) -> int:
        i = 1 if x > 0 else -1
        x = i * x

        result = 0
        while x > 0:
            result = result * 10 + x % 10
            x = x // 10

        return i * result if result < 2 ** 31 else 0
