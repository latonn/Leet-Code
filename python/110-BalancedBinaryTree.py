# Time:  O(n)
# Space: O(h)

# Given a binary tree, determine if it is height-balanced.
# For this problem, a height-balanced binary tree is defined as:
#
# a binary tree in which the depth of the two subtrees of every
# node never differ by more than 1.
#
# Example 1:
# Given the following tree [3,9,20,null,null,15,7]:
#
#     3
#    / \
#   9  20
#     /  \
#    15   7
# Return true.
#
# Example 2:
# Given the following tree [1,2,2,3,3,null,null,4,4]:
#
#        1
#       / \
#      2   2
#     / \
#    3   3
#   / \
#  4   4
# Return false.

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        # latonn's
        def depth(node):
            if not node:
                return 0
            left_depth, right_depth = depth(node.left), depth(node.right)
            if left_depth < 0 or right_depth < 0 or abs(left_depth - right_depth) > 1:
                return -1
            return max(left_depth, right_depth) + 1
        return depth(root) >= 0

    # kamyu's
    #     return self.getHeight(root) >= 0
    #
    # def getHeight(self, root):
    #     if root is None:
    #         return 0
    #     left_height, right_height = self.getHeight(root.left), self.getHeight(root.right)
    #     if left_height < 0 or right_height < 0 or abs(left_height - right_height) > 1:
    #         return -1
    #     return max(left_height, right_height) + 1


if __name__ == '__main__':
    root, root.left, root.right = TreeNode(1), TreeNode(2), TreeNode(2)
    root.left.left, root.left.right = TreeNode(3), TreeNode(3)
    root.left.left.left, root.left.left.right = TreeNode(4), TreeNode(4)

    print(Solution().isBalanced(root))



