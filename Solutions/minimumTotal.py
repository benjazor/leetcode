# NAME : Triangle
# LINK : https://leetcode.com/explore/challenge/card/april-leetcoding-challenge-2021/595/week-3-april-15th-april-21st/3715/
# DATE : 21/04/2021

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        result = [0] * (len(triangle) + 1)
        for i in range(len(triangle)):
            for j in range(len(triangle[-i - 1])):
                result[j] = triangle[-i - 1][j] + min(result[j], result[j + 1])
        return result[0]
