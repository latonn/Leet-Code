# Time:  O(m * n)
# Space: O(1)

# Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.
#
# Example 1:
#
# Input:
# [
#  [ 1, 2, 3 ],
#  [ 4, 5, 6 ],
#  [ 7, 8, 9 ]
# ]
#
# Output: [1,2,3,6,9,8,7,4,5]
#
# Example 2:
#
# Input:
# [
#   [1, 2, 3, 4],
#   [5, 6, 7, 8],
#   [9,10,11,12]
# ]
#
# Output: [1,2,3,4,8,12,11,10,9,5,6,7]


class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        # latonn's
        if not matrix:
            return []

        result = []
        xLeft, xRight, yTop, yBot = 0, len(matrix[0])-1, 0, len(matrix)-1

        while len(result) != len(matrix)*len(matrix[0]):
            for i in range(xLeft, xRight + 1):
                result.append(matrix[yTop][i])
            for i in range(yTop + 1, yBot):
                result.append(matrix[i][xRight])
            for i in reversed(range(xLeft, xRight + 1)):
                if yTop < yBot:
                    result.append(matrix[yBot][i])
            for i in reversed(range(yTop + 1, yBot)):
                if xLeft < xRight:
                    result.append(matrix[i][xLeft])
            xLeft, xRight, yTop, yBot = xLeft + 1, xRight - 1, yTop + 1, yBot - 1

        return result


if __name__ == '__main__':
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(Solution().spiralOrder(matrix))
