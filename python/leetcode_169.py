import random


class Solution:
    def majorityElement(self, nums: list[int]) -> int:  # 投票算法
        count = 0
        candidate = 0
        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)
        return candidate

    def majorityElement2(self, nums: list[int]) -> int:  # 随机算法
        length = len(nums)
        while True:
            ran_index = random.randint(0, length - 1)
            ran_num = nums[ran_index]
            count = 0
            for i in range(length):
                if nums[i] == ran_num:
                    count += 1
            if count > length // 2:
                return ran_num

solution = Solution()
print(solution.majorityElement([2,2,1,1,1,2,2]))