# KMP算法练习
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) > len(haystack):
            return -1
        if not needle:
            return 0
        if not haystack:
            return -1
        next_arr = self.get_next_arr(list(needle))
        ptr_1 = 0
        ptr_2 = 0
        while ptr_1 < len(haystack) and ptr_2 < len(needle):
            if haystack[ptr_1] == needle[ptr_2]:
                ptr_1 += 1
                ptr_2 += 1
            elif ptr_2 == 0:
                ptr_1 += 1
            else:
                ptr_2 = next_arr[ptr_2]
        return ptr_1 - ptr_2 if ptr_2 == len(needle) else -1

    def get_next_arr(self, nums: list):
        next_arr = [0 for i in range(len(nums))]
        next_arr[0] = -1
        if len(nums) == 1:
            return next_arr
        next_arr[1] = 0
        index = 2
        flag = 0
        while index < len(nums):
            if nums[index - 1] == nums[flag]:
                flag += 1
                next_arr[index] = flag
                index += 1
            elif flag > 0:
                flag = next_arr[flag]
            else:
                next_arr[index] = 0
                index += 1
        return next_arr

solution = Solution()
print(solution.strStr("aabaaabaaac", "aabaaac"))