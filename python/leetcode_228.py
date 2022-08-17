class Solution:
    def summaryRanges(self, nums: list[int]) -> list[str]:
        res = list()
        length = len(nums)
        i = 0
        while i < length:
            left = nums[i]
            index = i
            find_right = False
            while index < length - 1:
                if nums[index + 1] > nums[index] + 1:
                    right = nums[index]
                    break
                index += 1
            if not find_right:
                right = nums[index]
            if left == right:
                res.append(str(left))
            else:
                res.append(str(left) + "->" + str(right))
            i = index + 1
        return res

solution = Solution()
print(solution.summaryRanges([1]))
