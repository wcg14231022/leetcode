class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        if n == 2:
            return "11"
        if n == 3:
            return "21"
        res = "21"
        for i in range(3, n):
            res = self.get_string(res)
        return res

    def get_string(self, string: str):
        res = ""
        index = 0
        while index < len(string):
            cur_idnex = index
            cur_char = string[cur_idnex]
            while index < len(string) and string[index] == cur_char:
                index += 1
            res = res + str(index - cur_idnex) + cur_char
        return res

solution = Solution()
print(solution.countAndSay(5))