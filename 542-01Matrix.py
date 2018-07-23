#

# Given a matrix consists of 0 and 1, find the distance of the nearest 0 for each cell.
#
# The distance between two adjacent cells is 1.
# Example 1:
# Input:
# 0 0 0
# 0 1 0
# 0 0 0
#
# Output:
# 0 0 0
# 0 1 0
# 0 0 0
#
# Example 2:
# Input:
# 0 0 0
# 0 1 0
# 1 1 1
#
# Output:
# 0 0 0
# 0 1 0
# 1 2 1
#
# Note:
# The number of elements of the given matrix will not exceed 10,000.
# There are at least one 0 in the given matrix.
# The cells are adjacent in only four directions: up, down, left and right.


class Solution(object):
    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        q = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    q.append([i, j])
                else:
                    matrix[i][j] = float('inf')

        while q:
            cur = q.pop(0)
            for d in dirs:
                i, j = cur[0] + d[0], cur[1] + d[1]
                if i < 0 or i >= len(matrix) or j < 0 or j >= len(matrix[0]) or matrix[i][j] <= matrix[cur[0]][cur[1]]:
                    continue
                matrix[i][j] = matrix[cur[0]][cur[1]] + 1
                q.append([i, j])

        return matrix


if __name__ == '__main__':
    matrix = [[0, 1, 0, 1, 1],
              [1, 1, 0, 0, 1],
              [0, 0, 0, 1, 0],
              [1, 0, 1, 1, 1],
              [1, 0, 0, 0, 1]]
    print(Solution().updateMatrix(matrix))
