class Solution:
    def generateMatrix(self, n: int) -> list[list[int]]:
        row = n - 1
        col = n - 1
        res_arr = [[0 for i in range(n)] for j in range(n)]
        left_up = [0, 0]
        right_down = [row, col]
        count = 1
        max_count = n * n
        while left_up[0] <= right_down[0] and left_up[1] <= right_down[1]:
            row_a = left_up[0]
            for index_a in range(left_up[1], right_down[1] + 1):
                if count > max_count:
                    break
                res_arr[row_a][index_a] = count
                count += 1
            col_a = right_down[1]
            for index_b in range(left_up[0] + 1, right_down[0] + 1):
                if count > max_count:
                    break
                res_arr[index_b][col_a] = count
                count += 1
            row_b = right_down[0]
            for index_c in range(right_down[1] - 1, left_up[1] - 1, -1):
                if count > max_count:
                    break
                res_arr[row_b][index_c] = count
                count += 1
            col_b = left_up[1]
            for index_d in range(right_down[0] - 1, left_up[0], -1):
                if count > max_count:
                    break
                res_arr[index_d][col_b] = count
                count += 1
            left_up[0] += 1
            left_up[1] += 1
            right_down[0] -= 1
            right_down[1] -= 1
        return res_arr

solution = Solution()
print(solution.generateMatrix(10))