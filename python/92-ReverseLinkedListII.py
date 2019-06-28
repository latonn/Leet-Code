#

# Reverse a linked list from position m to n. Do it in one-pass.
#
# Note: 1 ≤ m ≤ n ≤ length of list.
#
# Example:
#
# Input: 1->2->3->4->5->NULL, m = 2, n = 4
# Output: 1->4->3->2->5->NULL

# Definition for singly-linked list.


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        if self:
            return "{} -> {}".format(self.val, self.next)

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return head

        dummy = ListNode(0)
        dummy.next = head
        cur = dummy

        for i in range(m-1):
            cur = cur.next
        # print('test: ', cur.val)

        revStart = cur.next
        for i in range(m, n):
            tmp = cur.next
            cur.next = revStart.next
            revStart.next = revStart.next.next
            cur.next.next = tmp
            # print(head.__repr__())

        return dummy.next


if __name__ == '__main__':
    head = ListNode(1)
    head.next, head.next.next = ListNode(2), ListNode(3)
    head.next.next.next, head.next.next.next.next = ListNode(4), ListNode(5)
    m, n = 2, 5
    head = Solution().reverseBetween(head, m, n)
    print(head.__repr__())
