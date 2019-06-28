#

# Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:
#
# Integers in each row are sorted in ascending from left to right.
# Integers in each column are sorted in ascending from top to bottom.
# Example:
#
# Consider the following matrix:
#
# [
#   [1,   4,  7, 11, 15],
#   [2,   5,  8, 12, 19],
#   [3,   6,  9, 16, 22],
#   [10, 13, 14, 17, 24],
#   [18, 21, 23, 26, 30]
# ]
#
# Given target = 5, return true.
#
# Given target = 20, return false.


class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        # latonn's
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False

        j = len(matrix[0]) - 1
        for i in range(len(matrix)):
            while j >= 0 and matrix[i][j] > target:
                j -= 1
            if matrix[i][j] == target:
                return True
        return False


if __name__ == '__main__':
    matrix = [[1,   4,  7, 11, 15],
              [2,   5,  8, 12, 19],
              [3,   6,  9, 16, 22],
              [10, 13, 14, 17, 24],
              [18, 21, 23, 26, 30]]
    target = 26
    print(Solution().searchMatrix(matrix, target))

