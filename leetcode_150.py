"""
150. Evaluate Reverse Polish Notation
You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.

Evaluate the expression. Return an integer that represents the value of the expression.

Note that:

The valid operators are '+', '-', '*', and '/'.
Each operand may be an integer or another expression.
The division between two integers always truncates toward zero.
There will not be any division by zero.
The input represents a valid arithmetic expression in a reverse polish notation.
The answer and all the intermediate calculations can be represented in a 32-bit integer.

"""
# Intuition: If Num put in stack if operation pop 2 elements do the operation and again put on stack.
# Space O(n)- for stack and O(4) for 4 operations
# Time: O(2n) - Putting and popping each element once.
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = deque()
        operations = {'+', '-', '*', '/'}

        for item in tokens:
            if item not in operations:
                stack.append(int(item))

            if item in operations:
                val2 = stack.pop()
                val1 = stack.pop()
                if item == '+':
                    calculated_val = val1 + val2

                elif item == '-':
                    calculated_val = val1 - val2

                elif item == '*':
                    calculated_val = val1 * val2
                else:
                    calculated_val = int(val1 / val2)

                stack.append(calculated_val)

        return stack[0]
