#

# You are given two non-empty linked lists representing two non-negative integers. The most significant digit comes
# first and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
#
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.
#
# Follow up:
# What if you cannot modify the input lists? In other words, reversing the lists is not allowed.
#
# Example:
#
# Input: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 8 -> 0 -> 7

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
        num1, num2 = [], []
        while l1:
            num1.append(l1.val)
            l1 = l1.next
        while l2:
            num2.append(l2.val)
            l2 = l2.next

        ans, carry, digit = [], 0, 0
        while num1 or num2:
            add1 = num1.pop() if num1 else 0
            add2 = num2.pop() if num2 else 0
            digit = (add1 + add2 + carry) % 10
            carry = int((add1 + add2 + carry) / 10)
            ans.insert(0, int(digit))

        while carry > 0:
            ans.insert(0, carry)
            carry = int(carry/10)

        head = ListNode(ans.pop(0))
        dummy = head
        while ans:
            node = ListNode(ans.pop(0))
            head.next = node
            head = head.next

        return dummy


if __name__ == '__main__':
    l1, l1.next, l1.next.next, l1.next.next.next = ListNode(7), ListNode(2), ListNode(4), ListNode(3)
    l2, l2.next, l2.next.next = ListNode(5), ListNode(6), ListNode(4)
    head = Solution().addTwoNumbers(l1, l2)
    while head:
        print(head.val)
        head = head.next