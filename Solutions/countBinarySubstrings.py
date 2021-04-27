# NAME : Count Binary Substrings
# LINK : https://leetcode.com/explore/challenge/card/april-leetcoding-challenge-2021/596/week-4-april-22nd-april-28th/3718/
# DATE : 27/04/2021

class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        result = 0
        previous = 0
        current = 1

        for i in range(1, len(s)):
            if (s[i - 1] != s[i]):
                result += min(previous, current)
                previous = current
                current = 1
            else:
                current += 1

        return result + min(previous, current)
