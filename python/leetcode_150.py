import queue
import re


class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        que = list()
        for i in range(len(tokens)):
            if re.search(r"[0-9]", tokens[i], re.I):
                que.append(int(tokens[i]))
            else:
                numa = que.pop()
                numb = que.pop()
                if tokens[i] == "+":
                    que.append(numb + numa)
                if tokens[i] == "-":
                    que.append(numb - numa)
                if tokens[i] == "*":
                    que.append(numb * numa)
                if tokens[i] == "/":
                    que.append(int(numb / numa))
        return que.pop()

solution = Solution()
print(solution.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))