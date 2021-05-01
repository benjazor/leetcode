# NAME : Unique Paths III
# LINK : https://leetcode.com/problems/unique-paths-iii/
# DATE : 01/05/2021

class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:

        def pathsRec(x, y, grid, zero_count):
            if x < 0 or y < 0 or x == len(grid) or y == len(grid[0]) or grid[x][y] == -1:
                return 0

            if grid[x][y] == 2:
                return 1 if zero_count == -1 else 0

            grid[x][y] = -1
            zero_count -= 1

            result = \
                pathsRec(x + 1, y, grid, zero_count) +\
                pathsRec(x - 1, y, grid, zero_count) +\
                pathsRec(x, y + 1, grid, zero_count) +\
                pathsRec(x, y - 1, grid, zero_count)

            grid[x][y] = 0
            zero_count += 1

            return result

        x_start, y_start, zero_count = 0, 0, 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 0:
                    zero_count += 1
                elif grid[i][j] == 1:
                    x_start, y_start = i, j

        return pathsRec(x_start, y_start, grid, zero_count)
