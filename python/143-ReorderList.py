#

# Given a singly linked list L: L0→L1→…→Ln-1→Ln,
# reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…
#
# You may not modify the values in the list's nodes, only nodes itself may be changed.
#
# Example 1:
# Given 1->2->3->4, reorder it to 1->4->2->3.
#
# Example 2:
# Given 1->2->3->4->5, reorder it to 1->5->2->4->3.

# Definition for singly-linked list.


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        if self:
            return "{} -> {}".format(self.val, repr(self.next))


class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if head is None or head.next is None or head.next.next is None:
            return

        # using slow and fast to find the middle node of the linked list
        slow = fast = head
        while fast and fast.next:
            # print(slow.val, fast.val)
            slow = slow.next
            fast = fast.next.next
        # print(slow.val, fast.val)
        list1 = head
        list2 = slow.next
        slow.next = None

        # reverse the list2
        dummy = ListNode(float("-inf"))
        while list2:
            dummy.next, list2.next, list2 = list2, dummy.next, list2.next
        list2 = dummy.next
        # print(list2.__repr__)
        # print(list1.__repr__)

        # merge two linked list
        mlist1, mlist2 = list1, list2
        while mlist2:
            tmp1, tmp2 = mlist1.next, mlist2.next
            mlist1.next, mlist2.next = mlist2, tmp1
            mlist1, mlist2 = tmp1, tmp2


if __name__ == "__main__":
    head = ListNode(1)
    head.next, head.next.next, head.next.next.next, head.next.next.next.next = \
        ListNode(2), ListNode(3), ListNode(4), ListNode(5)
    Solution().reorderList(head)
    print(head.__repr__())
