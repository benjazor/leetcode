# NAME : Longest Word in Dictionary through Deleting
# LINK : https://leetcode.com/explore/challenge/card/february-leetcoding-challenge-2021/587/week-4-february-22nd-february-28th/3649/
# DATE : 21/02/2021


class Solution:
    def findLongestWord(self, s: str, d: List[str]) -> str:
        longestWord = ""
        d.sort()
        for word in d:
            if len(word) <= len(longestWord):
                continue
            deleted = 0
            for i in range(len(word)):
                for j in range(i + deleted, len(s)):
                    if word[i] == s[j]:
                        if i == len(word) - 1 and len(word) > len(longestWord):
                            longestWord = word
                        break
                    else:
                        deleted += 1
        return longestWord