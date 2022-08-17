class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        index_1 = m - 1
        index_2 = n - 1
        insert_index = m + n - 1
        while index_1 >= 0 or index_2 >= 0:
            if index_1 < 0:
                nums1[insert_index] = nums2[index_2]
                index_2 -= 1
            elif index_2 < 0:
                nums1[insert_index] = nums1[index_1]
                index_1 -= 1
            else:
                if nums1[index_1] >= nums2[index_2]:
                    nums1[insert_index] = nums1[index_1]
                    index_1 -= 1
                else:
                    nums1[insert_index] = nums2[index_2]
                    index_2 -= 1
            insert_index -= 1

solution = Solution()
arr1 = [1,2,3,0,0,0]
m = 3
arr2 = [2,5,6]
n = 3
solution.merge(arr1, m, arr2, n)
print(arr1)