# Time:  O(n)
# Space: O(h), h is height of binary tree

# Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).
#
# For example, this binary tree [1,2,2,3,4,4,3] is symmetric:
#
#     1
#    / \
#   2   2
#  / \ / \
# 3  4 4  3
#
# But the following [1,2,2,null,3,null,3] is not:
#
#     1
#    / \
#   2   2
#    \   \
#    3    3
#
# Note:
# Bonus points if you could solve it both recursively and iteratively.

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        # recursive solution
        def isSymmetricHelper(left, right):
            if not left and not right:
                return True
            if not left or not right or left.val != right.val:
                return False
            return isSymmetricHelper(left.left, right.right) and isSymmetricHelper(left.right, right.left)

        if not root:
            return True

        return isSymmetricHelper(root.left, root.right)

        # iterative soluton
        # if root is None:
        #     return True
        # stack = []
        # stack.append(root.left)
        # stack.append(root.right)
        #
        # while stack:
        #     p, q = stack.pop(), stack.pop()
        #
        #     if p is None and q is None:
        #         continue
        #
        #     if p is None or q is None or p.val != q.val:
        #         return False
        #
        #     stack.append(p.left)
        #     stack.append(q.right)
        #
        #     stack.append(p.right)
        #     stack.append(q.left)
        #
        # return True


if __name__ == '__main__':
    root = TreeNode(1)
    root.left, root.right = TreeNode(2), TreeNode(2)
    root.left.left, root.left.right = TreeNode(3), TreeNode(4)
    root.right.left, root.right.right = TreeNode(4), TreeNode(3)

    print(Solution().isSymmetric(root))
