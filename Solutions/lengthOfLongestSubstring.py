# NAME : Longest Substring Without Repeating Characters
# LINK : https://leetcode.com/explore/challenge/card/january-leetcoding-challenge-2021/579/week-1-january-1st-january-7th/3595/
# DATE : 07/01/2021

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longestSubstring = ""
        currentSubstring = ""
        for i in range(len(s)):
            currentSubstring = s[i]
            for j in range(i + 1, len(s)):
                if s[j] in currentSubstring:
                    break
                else:
                    currentSubstring += s[j]
            if len(currentSubstring) > len(longestSubstring):
                longestSubstring = currentSubstring
            currentSubstring = ""
        return len(longestSubstring)
