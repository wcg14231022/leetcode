import sys


class Solution:
    def minFallingPathSum(self, matrix: list[list[int]]) -> int:
        res = sys.maxsize
        m = len(matrix)
        n = len(matrix[0])
        dp = [[sys.maxsize for i in range(n)] for j in range(m)]
        for i in range(n):
            dp[0][i] = matrix[0][i]
        for i in range(1, m):
            for j in range(n):
                if j == 0:
                    dp[i][j] = min(dp[i - 1][j], dp[i - 1][j + 1]) + matrix[i][j] if j + 1 < n else dp[i - 1][j] + matrix[i][j]
                elif j == m - 1:
                    dp[i][j] = min(dp[i - 1][j], dp[i - 1][j - 1]) + matrix[i][j] if j - 1 >= 0 else dp[i - 1][j] + matrix[i][j]
                else:
                    dp[i][j] = min(min(dp[i - 1][j - 1], dp[i - 1][j]), dp[i - 1][j + 1]) + matrix[i][j]
        for num in dp[-1]:
            res = min(res, num)
        return res

    def minFallingPathSum2(self, matrix: list[list[int]]) -> int:  # 滚动数组优化
        res = sys.maxsize
        m = len(matrix)
        n = len(matrix[0])
        dp = [[sys.maxsize for i in range(n)] for j in range(2)]
        for i in range(n):
            dp[0][i] = matrix[0][i]
        for i in range(1, m):
            cur = i % 2
            pre = (i + 1) % 2
            for j in range(n):
                if j == 0:
                    dp[cur][j] = min(dp[pre][j], dp[pre][j + 1]) + matrix[i][j] if j + 1 < n else dp[pre][j] + matrix[i][j]
                elif j == m - 1:
                    dp[cur][j] = min(dp[pre][j], dp[pre][j - 1]) + matrix[i][j] if j - 1 >= 0 else dp[pre][j] + matrix[i][j]
                else:
                    dp[cur][j] = min(min(dp[pre][j - 1], dp[pre][j]), dp[pre][j + 1]) + matrix[i][j]
        for num in dp[(m - 1) % 2]:
            res = min(res, num)
        return res

solution = Solution()
print(solution.minFallingPathSum([[100,-42,-46,-41],[31,97,10,-10],[-58,-51,82,89],[51,81,69,-51]]))
print(solution.minFallingPathSum2([[100,-42,-46,-41],[31,97,10,-10],[-58,-51,82,89],[51,81,69,-51]]))
