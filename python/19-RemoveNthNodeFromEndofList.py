# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        # kamyu's
        dummy = ListNode(-1)
        dummy.next = head
        slow, fast = dummy, dummy

        for _ in range(n):
            fast = fast.next

        while fast.next:
            slow, fast = slow.next, fast.next

        slow.next = slow.next.next

        return dummy.next

        # # latonn's
        # if head is None:
        #     return
        #
        # dummy = ListNode(0)
        # dummy.next = head
        #
        # cnt = 0
        # slow = fast = dummy
        # # slow: 0, 1, 2, 3, 4, 5, ...
        # # fast: 0, 2, 4, 6, 8, 10, ...
        #
        # # get the total length of the linked list
        # while fast and fast.next:
        #     cnt += 1
        #     slow = slow.next
        #     fast = fast.next.next
        #
        # if fast is None:
        #     length = cnt * 2 - 1
        # else:
        #     length = cnt * 2
        #
        # removePosition = length - n  # the previous node of target
        # tmp = dummy
        # while removePosition > 0:
        #     tmp = tmp.next
        #     removePosition -= 1
        #
        # tmp.next = tmp.next.next if tmp.next.next else None
        #
        # return dummy.next
