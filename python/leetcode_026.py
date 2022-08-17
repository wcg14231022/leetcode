import sys
class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        if len(nums) == 0:
            return 0
        location_dict = [-sys.maxsize - 1, 0]
        for i in range(len(nums)):
            if nums[i] > location_dict[0]:
                nums[location_dict[1]] = nums[i]
                location_dict[0] = nums[i]
                location_dict[1] += 1
        return location_dict[1]

solution = Solution()
print(solution.removeDuplicates([1, 1]))