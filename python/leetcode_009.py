class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        if x < 10:
            return True
        num_str = str(x)
        left, right = 0, len(num_str) - 1
        while left <= right:
            if num_str[left] != num_str[right]:
                return False
            left += 1
            right -= 1
        return True

solution = Solution()
print(solution.isPalindrome(0))

# 不将整数转为字符串如何解决

class Solution2:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        if x < 10:
            return True
        reverse_num = 0
        while x > reverse_num:
            temp = x % 10
            reverse_num = reverse_num * 10 + temp
            x //= 10
        if x == reverse_num:
            return True
        if x == reverse_num // 10:
            return True
        return False



solution2 = Solution2()
print(solution2.isPalindrome(10))