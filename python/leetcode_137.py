class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        ans = 0
        for i in range(32):
            total = sum((num >> i) & 1 for num in nums)
            if total % 3:
                if i == 31:
                    ans -= (1 << 31)
                else:
                    ans |= (1 << i)
        return ans

solution = Solution()
print(solution.singleNumber([-2,-2,1,1,4,1,4,4,-4,-2]))
