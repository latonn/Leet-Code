#

# Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded
# by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four
# edges of the grid are all surrounded by water.
#
# Example 1:
#
# Input:
# 11110
# 11010
# 11000
# 00000
#
# Output: 1
# Example 2:
#
# Input:
# 11000
# 11000
# 00100
# 00011
#
# Output: 3


class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0

        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    count += 1
                    self.dfs(grid, len(grid), len(grid[0]), i, j)
        return count

    def dfs(self, graph, row, col, i, j):
        if graph[i][j] == '0':
            return

        graph[i][j] = '0'
        if i != 0:
            self.dfs(graph, row, col, i-1, j)
        if i != row - 1:
            self.dfs(graph, row, col, i+1, j)
        if j != 0:
            self.dfs(graph, row, col, i, j-1)
        if j != col - 1:
            self.dfs(graph, row, col, i, j+1)


if __name__ == '__main__':
    grid = [['1', '1', '0', '0', '0'],
            ['1', '1', '0', '0', '0'],
            ['0', '0', '1', '0', '0'],
            ['0', '0', '0', '1', '1']]
    print(Solution().numIslands(grid))