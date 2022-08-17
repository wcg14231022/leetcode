import time


class Solution:
    def climbStairs(self, n: int) -> int:   # 普通动态规划
        if n == 1:
            return 1
        dp = [0 for i in range(n + 1)]
        dp[0] = dp[1] = 1
        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]

    def climbStairs2(self, n: int) -> int:  # 优化版动态规划
        if n == 1:
            return 1
        pre_1 = pre_2 = 1
        ans = 1
        for i in range(2, n + 1):
            ans = pre_1 + pre_2
            pre_2 = pre_1
            pre_1 = ans
        return ans

    def climbStairs3(self, n: int) -> int:  # 暴力递归
        if n == 0:
            return 1
        if n < 0:
            return 0
        return self.climbStairs3(n - 1) + self.climbStairs3(n - 2)


solution = Solution()

time_1 = time.time()
print(solution.climbStairs(45))
time_2 = time.time()
print("time_1:{}".format(time_2 - time_1))
print(solution.climbStairs2(45))
time_3 = time.time()
print("time_2:{}".format(time_3 - time_2))
print(solution.climbStairs3(45))
time_4 = time.time()
print("time_2:{}".format(time_4 - time_3))