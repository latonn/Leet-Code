# Time:  O(n)
# Space: O(1)

# Given a binary tree, determine if it is a valid binary search tree (BST).
#
# Assume a BST is defined as follows:
#
# The left subtree of a node contains only nodes with keys less than the node's key.
# The right subtree of a node contains only nodes with keys greater than the node's key.
# Both the left and right subtrees must also be binary search trees.
#
# Example 1:
#
#     2
#    / \
#   1   3
# Binary tree [2,1,3], return true.
#
# Example 2:
#
#     1
#    / \
#   2   3
# Binary tree [1,2,3], return false.

# Definition for a binary tree node.


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        # latonn's
        if root is None:
            return True
        inOrderPath = []
        self.InOrderTraversal(root, inOrderPath)
        for i in range(len(inOrderPath) - 1):
            if inOrderPath[i] >= inOrderPath[i+1]:
                return False
        return True

    def InOrderTraversal(self, node, inOrderPath):
        if node is None:
            return
        self.InOrderTraversal(node.left, inOrderPath)
        inOrderPath.append(node.val)
        self.InOrderTraversal(node.right, inOrderPath)

        # kamyu's
        # Morris traversal ( Binary tree traversal with O(n) time complexity and O(1) space complexity )
        # prev, cur = None, root
        # while cur:
        #     if cur.left is None:
        #         if prev and prev.val >= cur.val:
        #             return False
        #         prev = cur
        #         cur = cur.right
        #     else:
        #         node = cur.left
        #         while node.right and node.right != cur:
        #             node = node.right
        #
        #         if node.right is None:
        #             node.right = cur
        #             cur = cur.left
        #         else:
        #             if prev and prev.val >= cur.val:
        #                 return False
        #             node.right = None
        #             prev = cur
        #             cur = cur.right
        #
        # return True


if __name__ == '__main__':
    root = TreeNode(10)
    root.left, root.right = TreeNode(5), TreeNode(15)
    root.right.left, root.right.right = TreeNode(6), TreeNode(20)
    print(Solution().isValidBST(root))
