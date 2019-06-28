#
#

# Given a Binary Search Tree and a target number, return true if there exist
# two elements in the BST such that their sum is equal to the given target.
#
# Example 1:
# Input:
#     5
#    / \
#   3   6
#  / \   \
# 2   4   7
#
# Target = 9
# Output: True
#
# Example 2:
# Input:
#     5
#    / \
#   3   6
#  / \   \
# 2   4   7
#
# Target = 28
# Output: False

# Definition for a binary tree node.


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        # latonn's
        path = []
        self.InOrderTraversal(root, path)
        print(path)
        for i in range(len(path)):
            print(path[i], k-path[i], path[i+1:])
            if k - path[i] in path[i+1:]:
                return True
        return False

    def InOrderTraversal(self, node, path):
        if node is None:
            return

        self.InOrderTraversal(node.left, path)
        path.append(node.val)
        self.InOrderTraversal(node.right, path)


if __name__ == '__main__':
    root = TreeNode(1)
    # root.left, root.right = TreeNode(-1), TreeNode(2)
    # root.left.left = TreeNode(-3)
    # root.right.right = TreeNode(4)
    target = 2
    print(Solution().findTarget(root, target))
