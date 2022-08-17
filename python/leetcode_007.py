class Solution:
    def reverse(self, x: int) -> int:
        max, min = 2**31 - 1, -2**31
        res = 0
        negative = True if x < 0 else False
        while x != 0:
            if res < min // 10 + 1 or res > max // 10:
                return 0
            temp = x % 10
            if negative and temp > 0:
                temp -= 10
            x = (x - temp) // 10
            res = res * 10 + temp
        return res


solution = Solution()
print(solution.reverse(-10))