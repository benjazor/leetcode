# NAME : Concatenation of Consecutive Binary Numbers
# LINK : https://leetcode.com/explore/challenge/card/january-leetcoding-challenge-2021/582/week-4-january-22nd-january-28th/3618/
# DATE : 28/01/2021


class Solution:
    def concatenatedBinary(self, n: int) -> int:
        result = 0
        i = 1
        while i <= n:
            result = ((result << (i.bit_length() % 1000000007)) + i) % 1000000007
            i += 1
        return result


# It's my first binary shift :D
# Thanks to https://youtu.be/ttlNQ6YrdGs