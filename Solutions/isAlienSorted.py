# NAME : Verifying an Alien Dictionary
# LINK : https://leetcode.com/explore/challenge/card/april-leetcoding-challenge-2021/594/week-2-april-8th-april-14th/3702/
# DATE : 09/04/2021

class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        if len(words) < 2:
            return True

        def inOrder(word1: str, word2: str) -> bool:
            if word1 == word2:
                return True
            for i in range(len(word1)):
                if order.index(word1[i]) < order.index(word2[i]):
                    return True
                if order.index(word1[i]) > order.index(word2[i]) or i + 1 >= len(word2):
                    return False
                if order.index(word1[i]) == order.index(word2[i]):
                    continue
            return True

        for i in range(1, len(words)):
            if not inOrder(words[i - 1], words[i]):
                return False
        return True
