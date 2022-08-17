import time


class Solution:
    last_res = list(list())
    temp = list()
    quick_dict = {}

    def numDecodings(self, s: str) -> int:
        if s[0] == "0":
            return 0
        return self.reverse(s, len(s) - 1)

    def reverse(self, string, index):
        if index == -1:
            self.last_res.append(self.temp)
            return 1
        if index < -1:
            return 0
        if string[index] != "0":
            a = self.reverse(string, index - 1)
            # if index in self.quick_dict:
            #     a = self.quick_dict[index]
            # else:
            #     a = self.reverse(string, index - 1)
            #     self.quick_dict[index] = a
            # self.temp.append(string[index: index + 1])
        else:
            a = 0
        if int(string[index]) <= 6:
            if index - 2 >= -1 and 0 < int(string[index - 1]) <= 2:
                b = self.reverse(string, index - 2)
                # if index in self.quick_dict:
                #     b = self.quick_dict[index]
                # else:
                #     b = self.reverse(string, index - 2)
                #     self.quick_dict[index] = b
                # self.temp.append(string[index - 1: index + 1])
            else:
                b = 0
        else:
            if index - 2 >= -1 and string[index - 1] == "1":
                b = self.reverse(string, index - 2)
                # if index in self.quick_dict:
                #     b = self.quick_dict[index]
                # else:
                #     b = self.reverse(string, index - 2)
                #     self.quick_dict[index] = b
                # self.temp.append(string[index - 1: index + 1])
            else:
                b = 0
        return a + b

    # 动态规划
    def numDecodings2(self, s: str) -> int:
        n = len(s)
        f = [1] + [0] * n
        for i in range(1, n + 1):
            if s[i - 1] != '0':
                f[i] += f[i - 1]
            if i > 1 and s[i - 2] != '0' and int(s[i - 2 : i]) <= 26:
                f[i] += f[i - 2]
        return f[n]

    #  动态规划 + 滚动数组
    def numDecodings3(self, s: str) -> int:
        n = len(s)
        a, b, c = 0, 1, 0
        for i in range(1, n + 1):
            c = 0
            if s[i - 1] != '0':
                c += b
            if i > 1 and s[i - 2] != '0' and int(s[i - 2 : i]) <= 26:
                c += a
            a, b = b, c
        return c

solution = Solution()
time_1 = time.time()
# print(solution.numDecodings("111111111111111111111111111111111111111111111"))
print(solution.numDecodings3("1111111111111111111111111111111111111111111"))
time_2 = time.time()
print(time_2 - time_1)
# print(solution.last_res)
# print(solution.numDecodings("21246"))