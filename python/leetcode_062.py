class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0 for j in range(n)] for i in range(m)]
        dp[0][0] = 1
        for i in range(m):
            for j in range(n):
                if i > 0 and j > 0:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
                elif i > 0:
                    dp[i][j] = dp[i - 1][j]
                elif j > 0:
                    dp[i][j] = dp[i][j - 1]
        return dp[m - 1][n - 1]

solution = Solution()
print(solution.uniquePaths(3, 2))
