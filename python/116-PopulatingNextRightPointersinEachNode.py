# Time:  O(n)
# Space: O(1)

# Given a binary tree
#
# struct TreeLinkNode {
#   TreeLinkNode *left;
#   TreeLinkNode *right;
#   TreeLinkNode *next;
# }
# Populate each next pointer to point to its next right node. If there is no next right node, the next pointer
# should be set to NULL.
#
# Initially, all next pointers are set to NULL.
#
# Note:
#
# You may only use constant extra space.
# Recursive approach is fine, implicit stack space does not count as extra space for this problem.
# You may assume that it is a perfect binary tree (ie, all leaves are at the same level, and every parent has
# two children).
# Example:
#
# Given the following perfect binary tree,
#
#      1
#    /  \
#   2    3
#  / \  / \
# 4  5  6  7
#
# After calling your function, the tree should look like:
#
#      1 -> NULL
#    /  \
#   2 -> 3 -> NULL
#  / \  / \
# 4->5->6->7 -> NULL

# Definition for binary tree with next pointer.


class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

    def __repr__(self):
        if self is None:
            return "Nil"
        else:
            return "{} -> {}".format(self.val, repr(self.next))


class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        # latonn's
        from collections import defaultdict

        if root is None:
            return

        level = defaultdict(list)
        self.LevelOrderTraversal(root, 1, level)
        # print(level)
        for i in level.keys():
            for j in range(len(level[i]) - 1):
                level[i][j].next = level[i][j+1]

    def LevelOrderTraversal(self, root, depth, level):
        if root is None:
            return

        level[depth].append(root)

        self.LevelOrderTraversal(root.left, depth + 1, level)
        self.LevelOrderTraversal(root.right, depth + 1, level)
        return level

        # kamyu's
        # solution 1, Time: O(n), Space: O(1)
        # head = root
        # while head:
        #     prev, cur, next_head = None, head, None
        #     while cur and cur.left:
        #         cur.left.next = cur.right
        #         if cur.next:
        #             cur.right.next = cur.next.left
        #         cur = cur.next
        #     head = head.left

        # solution 2, Time: O(n), Space: O(logn)
        # recursion
        # if root is None:
        #     return
        # if root.left:
        #     root.left.next = root.right
        # if root.right and root.next:
        #     root.right.next = root.next.left
        # self.connect(root.left)
        # self.connect(root.right)


if __name__ == '__main__':
    root = TreeLinkNode(1)
    root.left, root.right = TreeLinkNode(2), TreeLinkNode(3)
    root.left.left, root.left.right = TreeLinkNode(4), TreeLinkNode(5)
    root.right.left, root.right.right = TreeLinkNode(6), TreeLinkNode(7)
    Solution().connect(root)
    print(root)
    print(root.left)
    print(root.left.left)