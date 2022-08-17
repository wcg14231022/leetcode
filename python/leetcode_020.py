class Solution:
    def isValid(self, s: str) -> bool:
        stack = list()
        brackets_dict = {"(": ")", "[": "]", "{": "}"}
        for i in range(len(s)):
            if s[i] == "(" or s[i] == "[" or s[i] == "{":
                stack.append(s[i])
            else:
                if len(stack) == 0:
                    return False
                top = stack.pop()
                if s[i] != brackets_dict[top]:
                    return False
        if len(stack) == 0:
            return True
        else:
            return False

solution = Solution()
print(solution.isValid("["))