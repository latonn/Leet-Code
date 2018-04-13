# Time:  O(n)
# Space: O(h)

# Given a binary tree, find the leftmost value in the last row of the tree.
#
# Example 1:
# Input:
#
#     2
#    / \
#   1   3
#
# Output:
# 1
#
# Example 2:
# Input:
#
#         1
#        / \
#       2   3
#      /   / \
#     4   5   6
#        /
#       7
#
# Output:
# 7
# Note: You may assume the tree (i.e., the given root node) is not NULL.

# Definition for a binary tree node.


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        LOT = {}
        LOT = self.LevelOrderTraversal(root, 0, LOT)
        bottom = max(LOT.keys())
        return LOT[bottom][0].val

    def LevelOrderTraversal(self, node, depth, LOT):
        if node is None:
            return LOT

        if depth in LOT.keys():
            LOT[depth].append(node)
        else:
            LOT.setdefault(depth, [])
            LOT[depth].append(node)

        LOT = self.LevelOrderTraversal(node.left, depth+1, LOT)
        LOT = self.LevelOrderTraversal(node.right, depth+1, LOT)
        return LOT


if __name__ == '__main__':
    root = TreeNode(0)
    root.right = TreeNode(-1)
    # root.left, root.right = TreeNode(2), TreeNode(3)
    # root.left.left = TreeNode(4)
    # root.right.left, root.right.right = TreeNode(5), TreeNode(6)
    # root.right.left.left = TreeNode(7)

    print(Solution().findBottomLeftValue(root))