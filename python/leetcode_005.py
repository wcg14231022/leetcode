class Solution:
    def longestPalindrome(self, s: str) -> str:
        # 动态规划解法
        if len(s) == 1:
            return s
        length = len(s)
        max_length = 1
        begin = 0
        res_str = ""
        dp = [[False] * length for arr in range(length)]
        for i in range(length):
            dp[i][i] = True
        # 枚举字串的长度
        for sub_length in range(2, length + 1):
            # 枚举左边界
            for i in range(length - 1):
                j = i + sub_length - 1
                if j > length - 1:  # 右边界越界
                    break
                if s[i] != s[j]:
                    dp[i][j] = False
                else:
                    if j - i <= 1:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i + 1][j - 1]
                if dp[i][j]:
                    cur_length = j - i + 1
                    if cur_length > max_length:
                        max_length = cur_length
                        begin = i
        return s[begin: begin + max_length]


solution = Solution()
test_str = "aaaa"
print(solution.longestPalindrome(test_str))


# Manacher算法
class Solution2:
    def longestPalindrome(self, s: str) -> str:
        s = "#" + "#".join(list(s)) + "#"
        # 子串的开始结束位置
        start = 0
        end = 0
        center = 0  # 扩散的中心
        right_bound = -1  # 扩散的右边界
        # 记录每个位置的回文半径  回文半径至少都是1
        palindrome_radius = [1 for ele in range(len(s))]
        # 从左到右逐个扩散
        # 1、当i大于right_bound时  直接扩散
        # 2、当i小于right_bound时  直接获取答案
        # 3、当i等于right_bound时  尝试扩散出去
        for i in range(len(s)):
            if i < right_bound:  # i 在 right_bound 范围内时 需要进行判断
                sys_radius = palindrome_radius[2 * center - i]
                # 对称位置扩散出去的边界是否达到了center位置扩散出去的位置的左边界 若未达到则直接获得答案
                if 2 * center - i - sys_radius + 1 > center - palindrome_radius[center] + 1:
                    palindrome_radius[i] = palindrome_radius[2 * center - i]
                # 尝试扩散出去  注意开始扩散出去的位置不能超出当前center的左边界 也不能超过右边界
                else:
                    temp_radius = self.expand(s, 2 * i - right_bound - 1, right_bound + 1)
                    temp_bound = i + temp_radius - 1
                    palindrome_radius[i] = temp_radius if temp_radius > sys_radius else sys_radius
                    if temp_bound > right_bound:
                        right_bound = temp_bound
                        center = i
            elif i > right_bound:
                center = i
                palindrome_radius[i] = self.expand(s, i, i)
                right_bound = center + palindrome_radius[i] - 1
            else:
                palindrome_radius[i] = self.expand(s, i, i)
                temp_bound = i + palindrome_radius[i] - 1
                if temp_bound > right_bound:
                    right_bound = temp_bound
                    center = i
            # 判断子串长度是否大于start、end子串的长度
            if palindrome_radius[i] * 2 - 1 > end - start + 1:
                start = i - palindrome_radius[i] + 1
                end = i + palindrome_radius[i] - 1
                test_str = s[start:end]
        # print(s[start:end])
        return s[start + 1: end + 1: 2]

    def expand(self, s, left, right) -> int:
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return (right - left) // 2

solution2 = Solution2()
test_str = "babadada"
print(solution2.longestPalindrome(test_str))

