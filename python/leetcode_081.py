class Solution:
    def search(self, nums: list[int], target: int) -> bool:
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return True
            elif nums[left] == nums[mid] and nums[mid] == nums[right]:
                left += 1
                right -= 1
            elif nums[left] <= nums[mid]:  # 可能在左边
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return True if nums[left] == target else False

solution = Solution()
print(solution.search([1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,1,1,1], 2))