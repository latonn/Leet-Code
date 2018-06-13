# Time:  O(n)
# Space: O(1)

# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse
# order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
#
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.
#
# Example
#
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.

# Definition for singly-linked list.


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # latonn's
        carry, sum = 0, 0
        ans = ListNode(0)
        tmp = ans
        h1, h2 = l1, l2

        while h1 and h2:
            sum = (h1.val + h2.val + carry) % 10
            carry = (h1.val + h2.val + carry) / 10
            tmp.next = ListNode(int(sum))
            h1, h2, tmp = h1.next, h2.next, tmp.next

        while h1:
            sum = (h1.val + carry) % 10
            carry = (h1.val + carry) / 10
            tmp.next = ListNode(int(sum))
            h1, tmp = h1.next, tmp.next

        while h2:
            sum = (h2.val + carry) % 10
            carry = (h2.val + carry) / 10
            tmp.next = ListNode(int(sum))
            h2, tmp = h2.next, tmp.next

        while int(carry):
            tmp.next = ListNode(int(carry))
            carry /= 10

        return ans.next

        # kamyu's
        # dummy = ListNode(0)
        # current, carry = dummy, 0
        #
        # while l1 or l2:
        #     val = carry
        #     if l1:
        #         val += l1.val
        #         l1 = l1.next
        #     if l2:
        #         val += l2.val
        #         l2 = l2.next
        #     carry, val = divmod(val, 10)
        #     current.next = ListNode(val)
        #     current = current.next
        #
        # if carry == 1:
        #     current.next = ListNode(1)
        #
        # return dummy.next


if __name__ == '__main__':
    l1, l1.next = ListNode(3), ListNode(7)
    l2, l2.next = ListNode(9), ListNode(2)
    ans = Solution().addTwoNumbers(l1, l2)
    print(ans.val)
    print(ans.next.val)
    print(ans.next.next.val)
