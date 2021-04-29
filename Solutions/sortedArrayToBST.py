# NAME : Convert Sorted Array to Binary Search Tree
# LINK : https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/
# DATE : 29/04/2021

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:

        def recursion(i: int, j: int) -> TreeNode:

            if i == j:
                return TreeNode(nums[i])

            if i > j:
                return None

            return TreeNode(
                nums[i + (j - i) // 2],
                recursion(i, i + (j - i) // 2 - 1),
                recursion(i + (j - i) // 2 + 1, j)
            )

        return recursion(0, len(nums) - 1)
