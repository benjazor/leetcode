# NAME : The K Weakest Rows in a Matrix
# LINK : https://leetcode.com/explore/challenge/card/february-leetcoding-challenge-2021/586/week-3-february-15th-february-21st/3641/
# DATE : 15/02/2021


class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        powers = {}
        for i in range(len(mat)):
            powers[i] = sum(mat[i])
        powers = sorted(powers, key=powers.get)
        return powers[:k]