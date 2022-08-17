class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        row = len(matrix) - 1
        col = len(matrix[0]) - 1
        res_arr = [0 for i in range(len(matrix) * len(matrix[0]))]
        left_up = [0, 0]
        right_down = [row, col]
        count = 0
        max_count = len(matrix) * len(matrix[0])
        while left_up[0] <= right_down[0] and left_up[1] <= right_down[1]:
            row_a = left_up[0]
            for index_a in range(left_up[1], right_down[1] + 1):
                if count >= max_count:
                    break
                res_arr[count] = matrix[row_a][index_a]
                count += 1
            col_a = right_down[1]
            for index_b in range(left_up[0] + 1, right_down[0] + 1):
                if count >= max_count:
                    break
                res_arr[count] = matrix[index_b][col_a]
                count += 1
            row_b = right_down[0]
            for index_c in range(right_down[1] - 1, left_up[1] - 1, -1):
                if count >= max_count:
                    break
                res_arr[count] = matrix[row_b][index_c]
                count += 1
            col_b = left_up[1]
            for index_d in range(right_down[0] - 1, left_up[0], -1):
                if count >= max_count:
                    break
                res_arr[count] = matrix[index_d][col_b]
                count += 1
            left_up[0] += 1
            left_up[1] += 1
            right_down[0] -= 1
            right_down[1] -= 1
        return res_arr

solution = Solution()
print(solution.spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]]))