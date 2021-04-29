# NAME : Unique Paths II
# LINK : https://leetcode.com/explore/challenge/card/april-leetcoding-challenge-2021/596/week-4-april-22nd-april-28th/3723/
# DATE : 29/04/2021

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        memo = [[0 for i in range(len(obstacleGrid[0]))]
                for i in range(len(obstacleGrid))]

        def recursion(i: int, j: int) -> int:
            if i == len(obstacleGrid) or j == len(obstacleGrid[0]) or obstacleGrid[i][j]:
                return 0
            if i + 1 == len(obstacleGrid) and j + 1 == len(obstacleGrid[0]):
                return 1
            if memo[i][j] > 0:
                return memo[i][j]
            memo[i][j] = recursion(i, j + 1) + recursion(i + 1, j)
            return memo[i][j]

        return recursion(0, 0)
