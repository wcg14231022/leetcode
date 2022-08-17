import sys


class Solution:
    def minimumTotal(self, triangle: list[list[int]]) -> int:
        res = sys.maxsize
        length = len(triangle)
        dp = [[sys.maxsize for i in range(len(triangle[length - 1]))] for j in range(length)]  # dp[i]代表到第i行的最小路径和
        print(dp)
        dp[0][0] = triangle[0][0]
        for i in range(1, length):
            for j in range(i + 1):
                if j == 0:
                    dp[i][j] = dp[i - 1][j] + triangle[i][j]
                elif j == i:
                    dp[i][j] = dp[i - 1][j - 1] + triangle[i][j]
                else:
                    dp[i][j] = min(dp[i - 1][j], dp[i - 1][j - 1]) + triangle[i][j]
        for num in dp[length - 1]:
            res = min(res, num)
        return res

triangle = [[-1],[-2,-3]]
solution = Solution()
print(solution.minimumTotal(triangle))