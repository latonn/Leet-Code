#

# Given a linked list, swap every two adjacent nodes and return its head.
#
# Example:
#
# Given 1->2->3->4, you should return the list as 2->1->4->3.
# Note:
#
# Your algorithm should use only constant extra space.
# You may not modify the values in the list's nodes, only nodes itself may be changed.

# Definition for singly-linked list.


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        if self:
            return "{} -> {}".format(self.val, self.next)


class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head

        dummy, dummy.next = ListNode(0), head
        cur = dummy

        while cur.next and cur.next.next:
            tmp = cur.next.next
            cur.next.next = tmp.next
            tmp.next = cur.next
            cur.next = tmp
            cur = cur.next.next
        return dummy.next


if __name__ == "__main__":
    head = ListNode(1)
    head.next, head.next.next = ListNode(2), ListNode(3)
    head.next.next.next = ListNode(4)
    new_head = Solution().swapPairs(head)
    print(new_head.__repr__())
