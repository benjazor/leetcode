# EXERCICE : Kth Missing Positive Number
# LINK : https://leetcode.com/explore/challenge/card/january-leetcoding-challenge-2021/579/week-1-january-1st-january-7th/3594/
# DATE : 06/01/2021

class Solution:
    def findKthPositive(self, arr: [int], k: int) -> int:
        missing = []
        arr_index = 0
        arr_len = len(arr)
        for i in range(1, arr[arr_len - 1] + 1 + k):
            if len(missing) > k:
                break
            if arr_index < arr_len and i == arr[arr_index]:
                arr_index += 1
            else:
                missing.append(i)
        return missing[k - 1 if k - 1 > 0 else 0]


test_list = [2,3,4,7,11] # [1, 2, 3, 4]
test_k = 5 # 2
expected_result = 9 # 6
sol = Solution()
print(sol.findKthPositive(test_list, test_k) == expected_result, sol.findKthPositive(test_list, test_k), expected_result)
