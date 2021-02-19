# NAME : Minimum Remove to Make Valid Parentheses
# LINK : https://leetcode.com/explore/challenge/card/february-leetcoding-challenge-2021/586/week-3-february-15th-february-21st/3645/
# DATE : 19/02/2021


class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        countOpen = 0
        countClose = 0
        toPop = []
        k = len(s)
        for i in range(k):
            if s[i] == "(":
                countOpen += 1
            elif s[i] == ")":
                if countOpen > 0:
                    countOpen -= 1
                else:
                    toPop.append(i)

            if s[k - 1 - i] == ")":
                countClose += 1
            elif s[k - 1 - i] == "(":
                if countClose > 0:
                    countClose -= 1
                else:
                    toPop.append(k - 1 - i)
        if toPop != []:
            toPop.sort()
            while toPop != []:
                currPop = toPop.pop(-1)
                s = s[:currPop] + s[currPop + 1 :]
        return s
