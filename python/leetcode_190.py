class Solution:
    def reverseBits(self, n: int) -> int:  # 逐位颠倒
        res = 0
        for i in range(32):
            res = (res << 1) | (n & 1)
            n >>= 1
        return res

    def reverseBits2(self, n: int) -> int:  # 分治
        n = (n >> 16) | (n << 16)
        n = ((n & 0xff00ff00) >> 8) | ((n & 0x00ff00ff) << 8)
        n = ((n & 0xf0f0f0f0) >> 4) | ((n & 0x0f0f0f0f) << 4)
        n = ((n & 0xcccccccc) >> 2) | ((n & 0x33333333) << 2)
        n = ((n & 0xaaaaaaaa) >> 1) | ((n & 0x55555555) << 1)
        return n


solution = Solution()
print(solution.reverseBits(int("00000010100101000001111010011100", 2)))
print(solution.reverseBits2(int("00000010100101000001111010011100", 2)))
