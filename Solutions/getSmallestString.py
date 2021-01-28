# NAME : Smallest String With A Given Numeric Value
# LINK : https://leetcode.com/explore/challenge/card/january-leetcoding-challenge-2021/582/week-4-january-22nd-january-28th/3619/
# DATE : 28/01/2021


class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        result = ""
        for i in range(1, n + 1):
            val = min(26, k - (n - i))
            result = chr(96 + val) + result
            k = k - val

        return result
