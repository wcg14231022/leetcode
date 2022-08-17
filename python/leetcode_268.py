class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        n = len(nums) + 1
        res = 0
        for i in range(1, n):
            res ^= i
        for num in nums:
            res ^= num
        return res

solution = Solution()
print(solution.missingNumber([3,0,1]))