import sys


class Solution:
    def minFallingPathSum(self, grid: list[list[int]]) -> int:  # 超时
        m = len(grid)
        n = len(grid[0])
        max_num = sys.maxsize
        dp = [[max_num for i in range(n)] for j in range(m)]
        for i in range(n):
            dp[0][i] = grid[0][i]
        for i in range(1, m):
            for j in range(n):
                dp[i][j] = max_num
                for k in range(n):
                    if k != j:
                        dp[i][j] = min(dp[i][j], dp[i - 1][k] + grid[i][j])
        res = max_num
        for num in dp[-1]:
            res = min(res, num)
        return res

    def minFallingPathSum2(self, grid: list[list[int]]) -> int:  # 时间优化
        m = len(grid)
        n = len(grid[0])
        max_num = sys.maxsize
        dp = [[max_num for i in range(n)] for j in range(m)]
        i1, i2 = -1, -1  # 最小值及次小值的下标
        for i in range(n):
            dp[0][i] = grid[0][i]
            if (i1 == -1 and dp[0][i] < max_num) or dp[0][i] < dp[0][i1]:
                i2 = i1
                i1 = i
            elif (i2 == -1 and dp[0][i] < max_num) or dp[0][i] < dp[0][i2]:
                i2 = i
        for i in range(1, m):
            ti1, ti2 = -1, -1
            for j in range(n):
                dp[i][j] = max_num
                if j != i1:
                    dp[i][j] = dp[i - 1][i1] + grid[i][j]
                else:
                    dp[i][j] = dp[i - 1][i2] + grid[i][j]
                if (ti1 == -1 and dp[i][j] <= max_num) or dp[i][j] < dp[i][ti1]:
                    ti2 = ti1
                    ti1 = j
                elif (ti2 == -1 and dp[i][j] < max_num) or dp[i][j] < dp[i][ti2]:
                    ti2 = j
            i1 = ti1
            i2 = ti2
        res = max_num
        for num in dp[-1]:
            res = min(res, num)
        return res

solution = Solution()
print(solution.minFallingPathSum([[1,2,3],[4,5,6],[7,8,9]]))
print(solution.minFallingPathSum2([[1,2,3],[4,5,6],[7,8,9]]))