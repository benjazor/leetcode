# NAME : Letter Combinations of a Phone Number
# LINK : https://leetcode.com/explore/challenge/card/april-leetcoding-challenge-2021/594/week-2-april-8th-april-14th/3701/
# DATE : 08/04/2021

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        keyboard = {
            # <key>: (<start_ord>, <length>)
            "2": (ord("a"), 3),
            "3": (ord("d"), 3),
            "4": (ord("g"), 3),
            "5": (ord("j"), 3),
            "6": (ord("m"), 3),
            "7": (ord("p"), 4),
            "8": (ord("t"), 3),
            "9": (ord("w"), 4),
        }

        if len(digits) == 0:
            return []

        result = []
        for i in range(keyboard[digits[0]][0], keyboard[digits[0]][0] + keyboard[digits[0]][1]):
            result.append(chr(i))

        if len(digits) == 1:
            return result

        for i in range(1, len(digits)):
            newResult = []
            for j in range(keyboard[digits[i]][0], keyboard[digits[i]][0] + keyboard[digits[i]][1]):
                for s in result:
                    newResult.append(s + chr(j))
            result = newResult

        return sorted(result)
