# NAME : Best Time to Buy and Sell Stock with Transaction Fee
# LINK : https://leetcode.com/explore/challenge/card/march-leetcoding-challenge-2021/590/week-3-march-15th-march-21st/3674/
# DATE : 16/03/2021


class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        if len(prices) < 1:
            return 0
        noStock = 0
        oneStock = -prices[0]
        for i in range(1, len(prices)):
            noStock = max(noStock, oneStock + prices[i] - fee)
            oneStock = max(oneStock, noStock - prices[i])
        return noStock