class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:  # 迭代法
        length = 1 << len(nums)
        res = []
        nums = sorted(nums)
        for i in range(length):
            temp = []
            b_num = i
            flag = True
            for j in range(len(nums) - 1, -1, -1):
                if j > 0 and nums[j] == nums[j - 1]:
                    if (b_num >> 1) & 1 != 1 and b_num & 1 == 1:
                        flag = False
                        break
                if b_num & 1 == 1:
                    temp.append(nums[j])
                b_num >>= 1
            if flag:
                res.append(temp)
        return res

solution = Solution()
res_arr = solution.subsetsWithDup([4,4,4,1,4])
print(res_arr)
new_arr = []
[new_arr.append(i) for i in res_arr if i not in new_arr]
print(new_arr)
