class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        min = int(1e9)
        max_profit = 0
        for i in range(len(prices)):
            if prices[i] < min:
                min = prices[i]
            if prices[i] - min > max_profit:
                max_profit = prices[i] - min
        return max_profit

solution = Solution()
print(solution.maxProfit([7,6,4,3,1]))