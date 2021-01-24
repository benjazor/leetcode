# NAME : Merge k Sorted Lists
# LINK : https://leetcode.com/explore/challenge/card/january-leetcoding-challenge-2021/582/week-4-january-22nd-january-28th/3615/
# DATE : 24/01/2021

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        merged = []
        for list in lists:
            while list:
                merged.append(list.val)
                list = list.next
        if len(merged) < 1:
            return None
        merged.sort(reverse=1)
        result = ListNode(merged[0], None)
        for num in merged[1:]:
            result = ListNode(num, result)
        return result