class Solution:
    def findMin(self, nums: list[int]) -> int:  # 二分查找
        length = len(nums)
        if length == 1:
            return nums[0]
        if length == 2:
            return min(nums[0], nums[1])
        left = 0
        right = length - 1
        while left < right:
            mid = left + (right - left) // 2
            if mid - 1 >= 0 and nums[mid] < nums[mid - 1]:
                return nums[mid]
            if mid + 1 < length and nums[mid] > nums[mid + 1]:
                return nums[mid + 1]
            if mid == 0 and nums[mid] < nums[length - 1]:
                return nums[mid]
            if mid == length - 1 and nums[mid] > nums[0]:
                return nums[0]
            if nums[mid] < nums[right]:
                right = mid - 1
            else:
                left = mid + 1
        return nums[left]

    def findMin2(self, nums: list[int]) -> int:  # API
        return min(nums)

    def findMin3(self, nums: list[int]) -> int:  # 官解
        low, high = 0, len(nums) - 1
        while low < high:
            pivot = low + (high - low) // 2
            if nums[pivot] < nums[high]:
                high = pivot
            else:
                low = pivot + 1
        return nums[low]

solution = Solution()
print(solution.findMin([11,13,15,17]))