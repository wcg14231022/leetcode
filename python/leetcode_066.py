class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        length = len(digits)
        for i in range(length - 1, -1, -1):
            if digits[i] != 9:
                digits[i] += 1
                for j in range(i + 1, length):
                    digits[j] = 0
                return digits
        return [1] + [0] * length

solution = Solution()
print(solution.plusOne([9,9,9]))
