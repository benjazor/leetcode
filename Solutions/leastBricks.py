# NAME : Brick Wall
# LINK : https://leetcode.com/explore/challenge/card/april-leetcoding-challenge-2021/596/week-4-april-22nd-april-28th/3717/
# DATE : 27/04/2021

class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        gaps = {0: 0}

        for i in range(len(wall)):
            current_gap = 0

            for j in range(len(wall[i]) - 1):
                current_gap += wall[i][j]

                if current_gap in gaps:
                    gaps[current_gap] += 1
                else:
                    gaps[current_gap] = 1

        return len(wall) - gaps[max(gaps, key=gaps.get)]
