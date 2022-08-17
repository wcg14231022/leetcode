class Solution:
    def numSquares(self, n: int) -> int:  # 贪心
        ps = set([i * i for i in range(1, int(n ** 0.5) + 1)])

        def divisible(n, count):
            if count == 1:
                return n in ps
            for p in ps:
                if divisible(n - p, count - 1):
                    return True
            return False

        for count in range(1, n + 1):  # 次数从小到大进行尝试
            if divisible(n, count):
                return count

    def numSquares2(self, n: int) -> int:  # BFS
        ps = [i * i for i in range(1, int(n ** 0.5) + 1)][::-1]
        pset = set(ps)
        queue, cache = [n], {n : 1}
        while queue:
            val = queue.pop(0)
            if val in pset:
                return cache[val]
            for p in ps:
                if val - p > 0 and val - p not in cache:
                    queue.append(val - p)
                    cache[val- p] = cache[val] + 1
        return -1

solution = Solution()
print(solution.numSquares(12))