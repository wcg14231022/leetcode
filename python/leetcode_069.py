class Solution:
    def mySqrt(self, x: int) -> int:
        left = 0
        right = x
        while left < right:
            mid = left + (right - left) // 2
            if mid * mid == x:
                return mid
            if mid * mid > x:
                right = mid - 1
            else:
                left = mid + 1
        return left if left * left <= x else left - 1

solution = Solution()
print(solution.mySqrt(4))