import collections
import queue

dp = [[False] * 5 for arr in range(5)]
for i in range(4):
    dp[i][i] = True;
print(dp)

arr = [1 for ele in range(10)]
print(arr)
arr = ["#", "b", "#", "a", "#", "b", "#"]
print(arr[1:6:2])

strs = ["flower","flow","flight"]
print(min(strs))
print(max(strs))

print(">>>>>>>>>>>>>>")
print(-1 // 10 + 1)
