class Solution:
    def search(self, nums: list[int], target: int) -> int:
        if not nums:
            return -1
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            # 判断哪边是有序的  如何判断
            if nums[left] <= nums[mid]:  # 左边有序
                if nums[left] <= target < nums[mid]:  #  target在左边
                    right = mid - 1
                else:
                    left += 1
            else:  # 右边有序
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1

solution = Solution()
print(solution.search([5,1,3], 5))