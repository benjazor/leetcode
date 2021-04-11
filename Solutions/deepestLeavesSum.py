# NAME : Deepest Leaves Sum
# LINK : https://leetcode.com/explore/challenge/card/april-leetcoding-challenge-2021/594/week-2-april-8th-april-14th/3704/
# DATE : 11/04/2021

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        if not root:
            return 0

        if not root.left and not root.right:
            return root.val

        level = [root]
        nextLevel = []
        deepestSum = 0

        while level != []:
            levelSum = 0

            for node in level:
                levelSum += node.val
                if node.left:
                    nextLevel.append(node.left)
                if node.right:
                    nextLevel.append(node.right)

            deepestSum = levelSum

            level = nextLevel
            nextLevel = []
            levelSum = 0

        return deepestSum
