#

# Given an integer n, generate all structurally unique BST's (binary search trees) that store values 1 ... n.
#
# Example:
#
# Input: 3
# Output:
# [
#   [1,null,3,2],
#   [3,2,null,1],
#   [3,1,null,null,2],
#   [2,1,3],
#   [1,null,2,null,3]
# ]
# Explanation:
# The above output corresponds to the 5 unique BST's shown below:
#
#    1         3     3      2      1
#     \       /     /      / \      \
#      3     2     1      1   3      2
#     /     /       \                 \
#    2     1         2                 3

# Definition for a binary tree node.


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __repr__(self):
        if self:
            serial = []
            queue = [self]

            while queue:
                cur = queue[0]

                if cur:
                    serial.append(cur.val)
                    queue.append(cur.left)
                    queue.append(cur.right)
                else:
                    serial.append("#")

                queue = queue[1:]

            while serial[-1] == "#":
                serial.pop()

            return repr(serial)

        else:
            return None


class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if n == 0:
            return []
        return self.generateTreesHelper(1, n)

    def generateTreesHelper(self, left, right):
        result = []
        if left > right:
            result.append(None)
            print('result: (early stop)', result)
            return result

        for i in range(left, right + 1):
            print('i: ', i)
            leftList = self.generateTreesHelper(left, i-1)
            rightList = self.generateTreesHelper(i+1, right)
            print('left list: ', leftList)
            print('right list: ', rightList)
            for j in leftList:
                for k in rightList:
                    root = TreeNode(i)
                    root.left = j
                    root.right = k
                    result.append(root)
                    print('result: ', result)
        return result


if __name__ == '__main__':
    n = 3
    print(Solution().generateTrees(n))
