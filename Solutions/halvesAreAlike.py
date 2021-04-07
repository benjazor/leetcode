# NAME : Determine if String Halves Are Alike
# LINK : https://leetcode.com/explore/challenge/card/april-leetcoding-challenge-2021/593/week-1-april-1st-april-7th/3699/
# DATE : 07/04/2021

class Solution:
    def halvesAreAlike(self, s: str) -> bool:

        count = 0
        vowels = "aeiou"

        s = s.lower()
        for i in range(len(s) // 2):
            if s[i] in vowels:
                count += 1
            if s[-i - 1] in vowels:
                count -= 1

        return not count
