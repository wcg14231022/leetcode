class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        min_str = min(strs)
        max_str = max(strs)
        for i, x in enumerate(min_str):
            if x != max_str[i]:
                return min_str[0: i]
        return min_str

solution = Solution()
print(solution.longestCommonPrefix(["dog","racecar","car"]))