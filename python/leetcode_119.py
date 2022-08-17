class Solution:
    def getRow(self, rowIndex: int) -> list[int]:  # 杨辉三角2
        res_arr = list()
        for i in range(rowIndex + 1):
            temp_arr = [0 for _ in range(i + 1)]
            temp_arr[0] = 1
            temp_arr[i] = 1
            for j in range(1, i):
                temp_arr[j] = res_arr[j - 1] + res_arr[j]
            res_arr = temp_arr
        return res_arr

solution = Solution()
print(solution.getRow(3))
