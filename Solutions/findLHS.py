# NAME : Longest Harmonious Subsequence
# LINK : https://leetcode.com/explore/challenge/card/february-leetcoding-challenge-2021/584/week-1-february-1st-february-7th/3628/
# DATE : 04/02/2021


class Solution:
    def findLHS(self, nums: List[int]) -> int:
        nums_dict = {}
        for num in nums:
            if num in nums_dict:
                nums_dict[num] += 1
            else:
                nums_dict[num] = 1
        result = 0
        last = None
        for num in sorted(nums_dict):
            if (
                last != None
                and abs(last - num) == 1
                and nums_dict[last] + nums_dict[num] > result
            ):
                result = nums_dict[last] + nums_dict[num]
            last = num
        return result