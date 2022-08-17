class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [[0 for i in range(n)] for j in range(m)]
        dp[0][0] = 1
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                elif i > 0 and j > 0:
                    dp[i][j] = dp[i][j - 1] + dp[i - 1][j]
                elif i > 0:
                    dp[i][j] = dp[i - 1][j]
                elif j > 0:
                    dp[i][j] = dp[i][j - 1]
        return dp[m - 1][n - 1]

solution = Solution()
obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
print(solution.uniquePathsWithObstacles(obstacleGrid))