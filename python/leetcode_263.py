class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False
        my_list = [2, 3, 5]
        for num in my_list:
            while n % num == 0:
                n //= num
        return n == 1

solution = Solution()
print(solution.isUgly(6))