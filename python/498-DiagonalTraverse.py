#

# Given a matrix of M x N elements (M rows, N columns), return all elements of the matrix in diagonal order as shown in
# the below image.
#
# Example:
# Input:
# [
#  [ 1, 2, 3 ],
#  [ 4, 5, 6 ],
#  [ 7, 8, 9 ]
# ]
# Output:  [1,2,4,7,5,3,6,8,9]
# Explanation:
#
# Note:
# The total number of elements of the given matrix will not exceed 10,000.


class Solution(object):
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        x = y = d = 0
        z = [[-1, 1], [1, -1]]  # right-up / left-down
        result = []

        if not matrix:
            return result

        for i in range(len(matrix) * len(matrix[0])):
            # print(x, y)
            result.append(matrix[x][y])
            x += z[d][0]
            y += z[d][1]

            if x >= len(matrix):
                x = len(matrix) - 1
                y += 2
                d = d ^ 1
            elif y >= len(matrix[0]):
                y = len(matrix[0]) - 1
                x += 2
                d = d ^ 1
            elif x < 0:
                x = 0
                d = d ^ 1
            elif y < 0:
                y = 0
                d = d ^ 1
        return result


if __name__ == "__main__":
    matrix = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]
    print(Solution().findDiagonalOrder(matrix))

