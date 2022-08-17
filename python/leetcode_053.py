class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        max_num = nums[0]
        sum = 0
        for index in range(len(nums)):
            sum += nums[index]
            if sum > max_num:
                max_num = sum
            if sum < 0:
                sum = 0
        return max_num

solution = Solution()
print(solution.maxSubArray([1,2,-1,-2,2,1,-2,1]))

# 尝试动态规划解
class Solution2:
    def maxSubArray(self, nums: list[int]) -> int:
        dp = [0 for i in range(len(nums))]
        dp[0] = nums[0]
        max_num = dp[0]
        for index in range(1, len(nums)):
            dp[index] = max(nums[index], dp[index - 1] + nums[index])
            if dp[index] > max_num:
                max_num = dp[index]
        return max_num

solution2 = Solution2()
print(solution2.maxSubArray([1,2,-1,-2,2,1,-2,1]))

# 分治法
class Solution3:
    class Status:
        def __init__(self, l_sum=None, r_sum=None, m_sum=None, i_sum=None):
            self.l_sum = l_sum
            self.r_sum = r_sum
            self.m_sum = m_sum
            self.i_sum = i_sum

    def maxSubArray(self, nums: list[int]) -> int:
        return Solution3.get_status(self, nums, 0, len(nums) - 1).m_sum

    def get_status(self, nums, left, right):
        if left == right:
            return Solution3.Status(nums[left], nums[left], nums[left], nums[left])
        mid = left + (right - left) // 2
        l_status = Solution3.get_status(self, nums, left, mid)
        r_status = Solution3.get_status(self, nums, mid + 1, right)
        return Solution3.push_up(self, l_status, r_status)

    def push_up(self, l_status: Status, r_status: Status):
        l_sum = max(l_status.l_sum, l_status.i_sum + r_status.l_sum)
        r_sum = max(r_status.r_sum, r_status.i_sum + l_status.r_sum)
        m_sum = max(l_status.r_sum + r_status.l_sum, max(l_status.m_sum, r_status.m_sum))
        i_sum = l_status.i_sum + r_status.i_sum
        return Solution3.Status(l_sum, r_sum, m_sum, i_sum)

solution3 = Solution3()
print(solution3.maxSubArray([1,2,-1,-2,2,1,-2,1]))