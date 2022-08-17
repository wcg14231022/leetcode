class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row = len(matrix)
        col = len(matrix[0])
        row_arr = []
        col_arr = []
        for i in range(row):
            for j in range(col):
                if matrix[i][j] == 0:
                    row_arr.append(i)
                    col_arr.append(j)
        for i in range(row):
            for j in range(col):
                if matrix[i][j] != 0 and (i in row_arr or j in col_arr):
                    matrix[i][j] = 0
        # return matrix

solution = Solution()
print(solution.setZeroes([[0,1,2,0],[3,4,5,2],[1,3,1,5]]))