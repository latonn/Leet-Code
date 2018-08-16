# Time:  O(n)
# Space: O(h)

# Given a Binary Search Tree (BST),
# convert it to a Greater Tree such that every key of
# the original BST is changed to the original key plus sum of
# all keys greater than the original key in BST.
#
# Example:
#
# Input: The root of a Binary Search Tree like this:
#               5
#             /   \
#           2     13
#
# Output: The root of a Greater Tree like this:
#              18
#             /   \
#           20     13

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        def convertBSTHelp(root, curr_sum):
            if not root:
                return curr_sum
            if root.right:
                curr_sum = convertBSTHelp(root.right, curr_sum)
            curr_sum += root.val
            root.val = curr_sum
            if root.left:
                curr_sum = convertBSTHelp(root.left, curr_sum)
            return curr_sum
        convertBSTHelp(root, 0)
        return root


if __name__ == '__main__':
    root = TreeNode(5)
    root.left = TreeNode(2)
    root.right = TreeNode(13)
    Solution().convertBST(root)

    print(root.left.val, root.val, root.right.val)

