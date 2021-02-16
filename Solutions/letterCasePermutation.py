# NAME : Letter Case Permutation
# LINK : https://leetcode.com/explore/challenge/card/february-leetcoding-challenge-2021/586/week-3-february-15th-february-21st/3642/
# DATE : 16/02/2021


class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        result = [S]
        k = len(S)
        for i in range(k):
            if ord(S[i]) >= ord("0") and ord(S[i]) <= ord("9"):
                continue
            if ord(S[i]) >= ord("A") and ord(S[i]) <= ord("Z"):
                to_append = []
                for r in result:
                    new_string = r[0:i] + chr(ord(S[i]) + 32) + r[i + 1 : k]
                    to_append.append(new_string)
                for string in to_append:
                    result.append(string)
                continue
            if ord(S[i]) >= ord("a") and ord(S[i]) <= ord("z"):
                to_append = []
                for r in result:
                    new_string = r[0:i] + chr(ord(S[i]) - 32) + r[i + 1 : k]
                    to_append.append(new_string)
                for string in to_append:
                    result.append(string)
                continue
        return result


# Easier to read
class Solution2:
    def letterCasePermutation(self, S: str) -> List[str]:
        result = [S]
        k = len(S)
        for i in range(k):
            if ord(S[i]) >= ord("0") and ord(S[i]) <= ord("9"):
                continue
            if ord(S[i]) >= ord("A") and ord(S[i]) <= ord("Z"):
                x = 32
            elif ord(S[i]) >= ord("a") and ord(S[i]) <= ord("z"):
                x = -32
            to_append = []
            for r in result:
                new_string = r[0:i] + chr(ord(S[i]) + x) + r[i + 1 : k]
                to_append.append(new_string)
            for string in to_append:
                result.append(string)
        return result