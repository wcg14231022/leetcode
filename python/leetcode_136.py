class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        res = 0
        for i in range(len(nums)):
            res ^= nums[i]
        return res

solution = Solution()
print(solution.singleNumber([4,1,2,1,2]))