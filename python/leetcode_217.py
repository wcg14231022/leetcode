class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        num_set = set()
        for i in range(len(nums)):
            if nums[i] in num_set:
                return True
            num_set.add(nums[i])
        return False

solution = Solution()
print(solution.containsDuplicate([1,2,3,4]))