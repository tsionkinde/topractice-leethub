class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows = []
        colunms = []

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if (matrix[i][j] == 0):
                    rows.append(i)
                    colunms.append(j)

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if (i in rows or j in colunms):
                    matrix[i][j] = 0

        return matrix

        