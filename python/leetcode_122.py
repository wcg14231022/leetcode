class Solution:
    def maxProfit(self, prices: list[int]) -> int:  # 贪心
        max_profit = 0
        for i in range(len(prices)):
            if i - 1 >= 0 and prices[i] - prices[i - 1] > 0:
                max_profit += prices[i] - prices[i - 1]
        return max_profit

    def maxProfit2(self, prices: list[int]) -> int:  # 动态规划
        length = len(prices)
        dp = list(list(0 for j in range(2)) for i in range(length))
        dp[0][0] = 0
        dp[0][1] = -prices[0]
        for index in range(1, length):
            dp[index][0] = max(dp[index - 1][0], dp[index - 1][1] + prices[index])
            dp[index][1] = max(dp[index - 1][0] - prices[index], dp[index - 1][1])
        return dp[length - 1][0]

solution = Solution()
print(solution.maxProfit([7,1,5,3,6,4]))
print(solution.maxProfit2([7,1,5,3,6,4]))