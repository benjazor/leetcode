# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        if head.next == None:
            return 2 * head.val
        else:
            return 2 * head.val + 2 * self.getDecimalValue(head.next)

test = ListNode(1, ListNode(0, ListNode(0, ListNode(1, ListNode(0, ListNode(0, ListNode(1, ListNode(1, ListNode(1, ListNode(0, ListNode(0, ListNode(0, ListNode(0, ListNode(0, ListNode(0, None)))))))))))))))
sol=Solution()
print(sol.getDecimalValue(test))
