# NAME : N-ary Tree Preorder Traversal
# LINK : https://leetcode.com/explore/challenge/card/april-leetcoding-challenge-2021/595/week-3-april-15th-april-21st/3714/
# DATE : 20/04/2021

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if not root:
            return None
        result = []
        for node in root.children:
            result += self.preorder(node)
        return [root.val] + result
