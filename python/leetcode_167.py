class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:  # 双指针
        left = 0
        right = len(numbers) - 1
        while left < right:
            if numbers[left] + numbers[right] == target:
                return [left, right]
            if numbers[left] + numbers[right] < target:
                left += 1
            else:
                right -= 1