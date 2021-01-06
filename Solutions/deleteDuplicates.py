# NAME : Remove Duplicates from Sorted List II
# LINK : https://leetcode.com/explore/challenge/card/january-leetcoding-challenge-2021/579/week-1-january-1st-january-7th/3593/
# DATE : 05/01/2021

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class SolutionRecursive:
    def __init__(self):
        self.last = None

    def deleteDuplicates(self, head: ListNode) -> ListNode:
        # REMOVE ALL DUPES
        if head == None:
            return None

        if head.next != None and head.val == head.next.val:
            self.last = head.val
            return self.deleteDuplicates(head.next.next)

        if head.val != self.last:
            return ListNode(head.val, self.deleteDuplicates(head.next))

        return self.deleteDuplicates(head.next)
