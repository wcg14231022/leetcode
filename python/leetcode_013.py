class Solution:
    def romanToInt(self, s: str) -> int:
        num_dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        res_num = 0
        length = len(s)
        i = 0
        while i < length:
            if i + 1 < length and num_dict[s[i + 1]] > num_dict[s[i]]:
                res_num += (num_dict[s[i + 1]] - num_dict[s[i]])
                i += 2
            else:
                res_num += num_dict[s[i]]
                i += 1
        return res_num

solution = Solution()
print(solution.romanToInt("LVIII"))