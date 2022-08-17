import bisect

from sortedcontainers import SortedList
class Solution:
    def containsNearbyAlmostDuplicate(self, nums: list[int], k: int, t: int) -> bool:  # 滑动窗口 + 红黑树
        window = SortedList()
        for i in range(len(nums)):
            if i > k:
                window.remove(nums[i - 1 - k])
            window.add(nums[i])
            idx = bisect.bisect_left(window, nums[i])
            if idx > 0 and abs(window[idx] - window[idx - 1]) <= t:
                return True
            if idx < len(window) - 1 and abs(window[idx + 1] - window[idx]) <= t:
                return True
        return False

    def containsNearbyAlmostDuplicate2(self, nums: list[int], k: int, t: int) -> bool:  # 桶排序
        def getIdx(u):
            return ((u + 1) // size) - 1 if u < 0 else u // size

        map = {}
        size = t + 1
        for i, u in enumerate(nums):
            idx = getIdx(u)
            # 目标桶已存在(桶不为空)，说明前面已有[u - t, u + t]范围的数字
            if idx in map:
                return True
            l, r = idx - 1, idx + 1
            if l in map and abs(u - map[l]) <= t:
                return True
            if r in map and abs(u - map[r]) <= t:
                return True
            map[idx] = u
            if i >= k:
                map.pop(getIdx(nums[i - k]))
        return False