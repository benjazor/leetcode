# NAME : Check If All 1's Are at Least Length K Places Away
# LINK : https://leetcode.com/explore/challenge/card/january-leetcoding-challenge-2021/582/week-4-january-22nd-january-28th/3616/
# DATE : 25/01/2021


class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        if k == 0:
            return True
        counter = k
        for i in range(len(nums)):
            if nums[i]:
                if counter < k:
                    return False
                counter = 0
            else:
                counter += 1
        return True