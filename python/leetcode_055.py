class Solution:
    def canJump(self, nums: list[int]) -> bool:
        length = len(nums)
        dp = [[False for i in range(length)] for j in range(length)]
        for i in range(length):
            dp[i][i] = True
        for i in range(length):
            for j in range(i + 1, length):
                if nums[i] >= j - i:
                    dp[i][j] = True
                else:
                    for k in range(1, j - i + 1):
                        if dp[i][j - k] and nums[j - k] >= j - i:
                            dp[i][j] = True
        return dp[0][length - 1]

solution = Solution()
print(solution.canJump([2,3,1,1,4]))
