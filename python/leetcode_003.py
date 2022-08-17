class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = right = 0
        char_set = set()
        max_length = 0
        while left <= right < len(s):
            while s[right] in char_set:
                cur_length = len(char_set)
                max_length = cur_length if cur_length > max_length else max_length
                if left <= right:
                    char_set.remove(s[left])
                    left += 1
            char_set.add(s[right])
            right += 1
        return max(max_length, len(char_set))


str_s = " "
solution = Solution()
print(solution.lengthOfLongestSubstring(str_s))