# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head is None:
            return None

        dummy = ListNode(0)
        dummy.next = head

        prev, cur = head, head.next
        while cur:
            if prev.val == cur.val:
                prev.next = cur.next
            else:
                prev = prev.next
            cur = cur.next

        return dummy.next
