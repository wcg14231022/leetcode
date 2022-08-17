class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        length_s = len(s)
        length_t = len(t)
        if length_s != length_t:
            return False
        char_dict1 = dict()
        char_dict2 = dict()
        for i in range(length_s):
            char_s, char_t = s[i], t[i]
            if char_s not in char_dict1:
                char_dict1[char_s] = char_t
            if char_t not in char_dict2:
                char_dict2[char_t] = char_s
            if char_dict1[char_s] != char_t or char_dict2[char_t] != char_s:
                return False
        return True

solution = Solution()
print(solution.isIsomorphic("paper", "title"))