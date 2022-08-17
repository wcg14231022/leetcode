class Solution:
    def isAnagram(self, s: str, t: str) -> bool:  # 排序
        str_s = sorted(s)
        str_t = sorted(t)
        return str_s == str_t

    def isAnagram2(self, s: str, t: str) -> bool:  # 哈希表
        dict_s = dict()
        dict_t = dict()
        length_s = len(s)
        length_t = len(t)
        if length_s != length_t:
            return False
        for i in range(length_s):
            if not s[i] in dict_s:
                dict_s[s[i]] = 1
            else:
                dict_s[s[i]] += 1

        for j in range(length_t):
            if not t[j] in dict_t:
                dict_t[t[j]] = 1
            else:
                dict_t[t[j]] += 1

        for key in dict_s:
            if not key in dict_t:
                return False
            if dict_s[key] != dict_t[key]:
                return False
        return True

solution = Solution()
print(solution.isAnagram("anagram", "nagaram"))
print(solution.isAnagram2("anagram", "nagaram"))