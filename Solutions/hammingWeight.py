# NAME : Number of 1 Bits
# LINK : https://leetcode.com/explore/challenge/card/february-leetcoding-challenge-2021/584/week-1-february-1st-february-7th/3625/
# DATE : 02/02/2021


class Solution:
    def hammingWeight(self, n: int) -> int:
        n = str(bin(n))[2:]
        result = 0
        for i in n:
            if i == "1":
                result += 1
        return result