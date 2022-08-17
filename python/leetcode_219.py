class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        nums_dict = dict()
        for i in range(len(nums)):
            if nums[i] in nums_dict:
                pre_index = nums_dict[nums[i]]
                distance = abs(i - pre_index)
                if distance <= k:
                    return True
                nums_dict[nums[i]] = i
            else:
                nums_dict[nums[i]] = i
        return False

solution = Solution()
print(solution.containsNearbyDuplicate([1,0,1,1], 1))