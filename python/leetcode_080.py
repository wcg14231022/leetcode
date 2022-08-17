class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        length = len(nums)
        if length <= 2:
            return length
        slow = fast = 2
        while fast < length:
            if nums[fast] != nums[slow - 2]:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1
        return slow

solution = Solution()
print(solution.removeDuplicates([0,0,1,1,1,1,2,3,3]))