import sys


class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dp = [[0 for i in range(n)] for j in range(m)]
        dp[0][0] = grid[0][0]
        for i in range(m):
            for j in range(n):
                if i > 0 and j > 0:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]
                elif i > 0:
                    dp[i][j] = dp[i - 1][j] + grid[i][j]
                elif j > 0:
                    dp[i][j] = dp[i][j - 1] + grid[i][j]
        return dp[m - 1][n - 1]

solution = Solution()
print(solution.minPathSum([[1,2,3],[4,5,6]]))