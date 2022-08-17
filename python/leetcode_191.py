class Solution:
    def hammingWeight(self, n: int) -> int:  # 全部遍历
        ret = sum(1 for i in range(32) if n & (1 << i))
        return ret

    def hammingWeight2(self, n: int) -> int:  # 位运算
        ret = 0
        while n:
            n &= (n - 1)
            ret += 1
        return ret


solution = Solution()
print(solution.hammingWeight(int("00000000000000000000000000001011", 2)))
print(solution.hammingWeight2(int("00000000000000000000000000001011", 2)))