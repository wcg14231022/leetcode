class Solution:
    def addBinary(self, a: str, b: str) -> str:
        int_a = int(a, 2)
        int_b = int(b, 2)
        while int_b:
            answer = int_a ^ int_b
            carry = (int_a & int_b) << 1
            int_a, int_b = answer, carry
        return bin(int_a)[2:]

solution = Solution()
print(solution.addBinary("11", "1"))