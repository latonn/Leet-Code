# Time:  O(n)
# Space: O(h)

# Given a binary tree, imagine yourself standing on the right side of it,
# return the values of the nodes you can see ordered from top to bottom.
#
# Example:
#
# Input: [1,2,3,null,5,null,4]
# Output: [1, 3, 4]
# Explanation:
#
#    1            <---
#  /   \
# 2     3         <---
#  \     \
#   5     4       <---

# Definition for a binary tree node.


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # latonn's
        result = []
        lot = self.levelOrderTraversal(root, 0, {})
        for i in range(len(lot)):
            result.append(lot[i][0].val)
        return result

    def levelOrderTraversal(self, node, depth, LOT):
        if node is None:
            return LOT

        if depth in LOT.keys():
            LOT[depth].append(node)
        else:
            LOT.setdefault(depth, [])
            LOT[depth].append(node)

        LOT = self.levelOrderTraversal(node.right, depth+1, LOT)
        LOT = self.levelOrderTraversal(node.left, depth+1, LOT)
        return LOT

        # kamyu's
    #     result = []
    #     self.rightSideViewDFS(root, 1, result)
    #     return result
    #
    # def rightSideViewDFS(self, node, depth, result):
    #     if not node:
    #         return
    #
    #     if depth > len(result):
    #         result.append(node.val)
    #
    #     self.rightSideViewDFS(node.right, depth+1, result)
    #     self.rightSideViewDFS(node.left, depth+1, result)


if __name__ == '__main__':
    root = TreeNode(1)
    root.left, root.right = TreeNode(2), TreeNode(3)
    root.left.right, root.right.right = TreeNode(5), TreeNode(4)
    print(Solution().rightSideView(root))
