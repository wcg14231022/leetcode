import time


class Solution:
    def countPrimes(self, n: int) -> int:  # 暴力统计  超时
        count = 0
        for i in range(n):
            if self.isPrimes(i):
                count += 1
        return count

    def isPrimes(self, n):
        if n < 2:
            return False
        if n == 2:
            return True
        end = int(n ** 0.5)
        for i in range(2, end + 1):
            div = n // i
            if n == div * i:
                return False
        return True

    def countPrimes2(self, n: int) -> int:  # 埃氏筛
        isprime = [1 for i in range(n)]
        ans = 0
        for i in range(2, n):
            if isprime[i] == 1:
                ans += 1
                if i * i < n:
                    for j in range(i * i, n, i):
                        isprime[j] = 0
        return ans

solution = Solution()
time1 = time.time()
print(solution.countPrimes2(1500000))
time2 = time.time()
print(time2 - time1)