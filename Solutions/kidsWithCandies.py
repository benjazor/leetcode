# NAME : Kids With the Greatest Number of Candies
# LINK : https://leetcode.com/problems/kids-with-the-greatest-number-of-candies
# DATE : 03/05/2021

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candies = max(candies)

        for i in range(len(candies)):
            candies[i] = candies[i] + extraCandies >= max_candies

        return candies
