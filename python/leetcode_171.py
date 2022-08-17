class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        length = len(columnTitle)
        res = 0
        for i in range(length - 1, -1, -1):
            res += (pow(26, length - 1 - i) * (ord(columnTitle[i]) - ord("A") + 1))
        return res

solution = Solution()
print(solution.titleToNumber("ZY"))