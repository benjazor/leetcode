# NAME : Check If Two String Arrays are Equivalent
# LINK : https://leetcode.com/explore/challenge/card/january-leetcoding-challenge-2021/580/week-2-january-8th-january-14th/3597/
# DATE : 08/01/2021

class Solution1:
    def arrayStringsAreEqual(self, word1: [str], word2: [str]) -> bool:
        return "".join(word1) == "".join(word2)


class Solution2:
    def arrayStringsAreEqual(self, word1: [str], word2: [str]) -> bool:
        word1_string, word2_string = "", ""
        for substring in word1:
            word1_string += substring
        for substring in word2:
            word2_string += substring
        return word1_string == word2_string
