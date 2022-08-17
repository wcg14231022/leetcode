class Solution:
    def intToRoman(self, num: int) -> str:
        str_list = ["I", "IV", "V", "IX", "X", "XL", "L", "XC", "C", "CD", "D", "CM", "M"]
        num_list = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
        res = ""
        for i in range(len(num_list) - 1, -1, -1):
            while num >= num_list[i]:
                res += str_list[i]
                num -= num_list[i]
        return res

solution = Solution()
print(solution.intToRoman(1994))