class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        maxArea = 0
        rows = []
        cols = []
        for i in range(0,len(matrix)):
            rowTemp = []
            colTemp = []
            for j in range(0, len(matrix[0])):
                rowTemp.append(0)
                colTemp.append(0)
            rows.append(rowTemp)
            cols.append(colTemp)
                
        for i in range(len(matrix)-1,-1,-1):
            for j in range(len(matrix[0])-1,-1,-1):
                area = 0
                if matrix[i][j]=='1':
                    if i==len(matrix)-1:
                        rows[i][j] = 1
                    else:
                        rows[i][j] = rows[i+1][j] + 1
                    if j == len(matrix[0])-1:
                        cols[i][j] = 1
                    else:
                        cols[i][j] = cols[i][j+1]+1
                    area = cols[i][j]
                    minCol = cols[i][j]
                for k in range(1, rows[i][j]):
                    if minCol > cols[i+k][j]:
                        minCol = cols[i+k][j]
                    if (k+1)*minCol > area:
                        area = (k+1)*minCol
                if maxArea < area:
                    maxArea = area
        return maxArea
