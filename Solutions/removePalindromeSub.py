# NAME : Remove Palindromic Subsequences
# LINK : https://leetcode.com/explore/challenge/card/march-leetcoding-challenge-2021/589/week-2-march-8th-march-14th/3665/
# DATE : 08/03/2021


class Solution:
    def removePalindromeSub(self, s: str) -> int:
        if s == "":
            return 0
        if s == s[::-1]:
            return 1
        return 2