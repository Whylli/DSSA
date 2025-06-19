from typing import List
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for t in tokens:
            if t not in {"+", "-", "*", "/"}:
                stack.append(int(t))
                continue
            b = stack.pop()
            a = stack.pop()
            match t:
                case "+":
                    p = a + b
                case "-":
                    p = a - b
                case "*":
                    p = a * b
                case "/":
                    p = int(a / b)
            stack.append(p)
        return stack[0]