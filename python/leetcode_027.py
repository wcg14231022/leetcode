import sys


class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        if len(nums) == 0:
            return 0
        location_list = list()
        same_count = 0
        used_location = list()
        for i in range(len(nums)):
            if nums[i] == val:
                same_count += 1
                location_list.append(i)
            else:
                if len(location_list) != 0 and not i in used_location:
                    nums[location_list.pop(0)] = nums[i]
                    location_list.append(i)
                    used_location.append(i)
        return len(nums) - same_count


nums = [0,1,2,2,3,0,4,2]
solution = Solution()
print(solution.removeElement(nums, 2))
print(nums)