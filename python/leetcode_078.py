class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:  # 位运算
        length = 1 << len(nums)
        res = []
        for i in range(length):
            if i == 0:
               res.append([])
            else:
                temp = []
                b_num = i
                for j in range(len(nums)):
                    if b_num & 1 == 1:
                        temp.append(nums[j])
                    b_num >>= 1
                res.append(temp)
        return res

    res_arr = list(list())
    add_arr = list()  # 每个分支都会到达递归出口，并且每次到达递归出口时，add_arr都是不一样的，此时将add_arr加入res_arr

    def subsets2(self, nums: list[int]) -> list[list[int]]:  # 暴力递归
        self.reverse(nums, 0)
        return self.res_arr

    def reverse(self, nums, index):
        if index == len(nums):
            self.res_arr.append(list(self.add_arr))
            return
        self.add_arr.append(nums[index])
        self.reverse(nums, index + 1)
        self.add_arr.pop(len(self.add_arr) - 1)
        self.reverse(nums, index + 1)

solution = Solution()
print(solution.subsets([0]))

print(solution.subsets2([0]))