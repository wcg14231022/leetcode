class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        start = len(s) - 1
        end = -1
        find_last = False
        for index in range(len(s) - 1, -1, -1):
            if s[index] != " " and not find_last:
                find_last = True
                start = index
            if s[index] == " " and find_last:
                end = index
                break
        return start - end

solution = Solution()
print(solution.lengthOfLastWord("   fly me   to   the moon  "))