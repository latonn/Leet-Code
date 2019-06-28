#

# Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.
#
# Example:
#
# Input:
# [
#   1->4->5,
#   1->3->4,
#   2->6
# ]
# Output: 1->1->2->3->4->4->5->6


# Definition for singly-linked list.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        import heapq
        heap = []
        for node in lists:
            if node:
                heapq.heappush(heap, (node.val, node))

        dummy = ListNode(-1)
        head = dummy
        while heap:
            smlNode = heapq.heappop(heap)[1]
            dummy.next = smlNode
            dummy = dummy.next
            if smlNode.next:
                heapq.heappush(heap, (smlNode.next.val, smlNode.next))
        return head.next


if __name__ == '__main__':
    l1, l1.next, l1.next.next = ListNode(1), ListNode(4), ListNode(5)
    l2, l2.next, l2.next.next = ListNode(1), ListNode(3), ListNode(4)
    l3, l3.next = ListNode(2), ListNode(6)
    lists = [ l1, l2, l3]
    result = Solution().mergeKLists(lists)
