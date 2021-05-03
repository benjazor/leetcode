# NAME : N-th Tribonacci Number
# LINK : https://leetcode.com/problems/n-th-tribonacci-number/
# DATE : 03/05/2021

class Solution:
    def tribonacci(self, n: int) -> int:
        memo = [-1 for i in range(n + 1)]

        def tribonacciRec(n: int) -> int:
            if n == 0:
                return n
            if n < 3:
                return 1

            if memo[n] > -1:
                return memo[n]

            memo[n] = tribonacciRec(
                n - 1) + tribonacciRec(n - 2) + tribonacciRec(n - 3)
            return memo[n]

        return tribonacciRec(n)
