class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and n & (n - 1) == 0

    def isPowerOfTwo2(self, n: int) -> bool:
        return n > 0 and n & (-n) == n

solution = Solution()
print(solution.isPowerOfTwo(10))
print(solution.isPowerOfTwo2(2))