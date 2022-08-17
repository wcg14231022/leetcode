class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        top = 0
        buttom = len(matrix) - 1
        while top < buttom:
            mid = top + (buttom - top) // 2
            if self.find_target(matrix[mid], target):
                return True
            if matrix[mid][len(matrix[mid]) - 1] < target:
                top = mid + 1
            else:
                buttom = mid - 1
        return True if self.find_target(matrix[top], target) else False

        pass

    def find_target(self, nums, target):
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return True
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return True if nums[left] == target else False

solution = Solution()
print(solution.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 13))