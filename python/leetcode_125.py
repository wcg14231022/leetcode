class Solution:
    def isPalindrome(self, s: str) -> bool:  # 简单解法
        left = 0
        right = len(s) - 1
        ignore_list = [" ", ",", ":", ".", "@", "#", "_", "(", ")", "[", "]", "{", "}", "'", "\\", "/", "\"", "-", "?", ";", "!", "`"]
        while left < right:
            while left < right and ignore_list.__contains__(s[left]):
                left += 1
            while left < right and ignore_list.__contains__(s[right]):
                right -= 1
            if not left < right:
                break
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
        return True

    def isPalindrome2(self, s: str) -> bool:  # 简单解法
        left = 0
        n = len(s)
        right = n - 1
        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1
            if left < right:
                if s[left].lower() != s[right].lower():
                    return False
                left += 1
                right -= 1
        return True

solution = Solution()
print(solution.isPalindrome(" "))