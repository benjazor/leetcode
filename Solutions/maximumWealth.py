# NAME : Richest Customer Wealth
# LINK : https://leetcode.com/problems/richest-customer-wealth/
# DATE : 03/05/2021

class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:

        for i in range(len(accounts)):
            wealth = 0
            for j in range(len(accounts[i])):
                wealth += accounts[i][j]
            accounts[i] = wealth

        return max(accounts)
