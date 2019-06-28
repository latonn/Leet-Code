# Time:  O(n)
# Space: O(1)

# Reverse a singly linked list.
#
# click to show more hints.
#
# Hint:
# A linked list can be reversed either iteratively or recursively. Could you implement both?

# Definition for singly-linked list.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        if self:
            return "{} -> {}".format(self.val, repr(self.next))


class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # jz version
        if head is None:
            return

        prev, cur = None, head
        while cur:
            tmp = cur.next
            cur.next = prev
            prev, cur = cur, tmp

        return prev

        # # solution 1
        # dummy = ListNode(float("-inf"))
        # while head:
        #     dummy.next, head.next, head = head, dummy.next, head.next
        # return dummy.next

        # solution 2
        # https: // goo.gl / MWBiAy
        # previous = None
        # current = head
        # preceding = head.next
        # while preceding:
        #     current.next = previous
        #     previous = current
        #     current = preceding
        #     preceding = preceding.next
        # current.next = previous
        # return current

    #     # recursive version
    #     if head is None:
    #         return
    #
    #     return self.recursive(head, None)
    #
    # def recursive(self, node, prev=None):
    #     if node is None:
    #         return prev
    #     tmp = node.next
    #     node.next = prev
    #     return self.recursive(tmp, node)


if __name__ == '__main__':
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    print(Solution().reverseList(head))

