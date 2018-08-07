#

# Implement a basic calculator to evaluate a simple expression string.
#
# The expression string may contain open ( and closing parentheses ), the plus + or minus sign -, non-negative integers
# and empty spaces .
#
# Example 1:
# Input: "1 + 1"
# Output: 2
#
# Example 2:
# Input: " 2-1 + 2 "
# Output: 3
#
# Example 3:
# Input: "(1+(4+5+2)-3)+(6+8)"
# Output: 23
#
# Note:
# You may assume that the given expression is always valid.
# Do not use the eval built-in library function.


class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        operands, operators = [], []
        operand = ""
        for i in reversed(range(len(s))):
            if s[i].isdigit():
                operand += s[i]
                if i == 0 or not s[i - 1].isdigit():
                    operands.append(int(operand[::-1]))
                    operand = ""
            elif s[i] == ')' or s[i] == '+' or s[i] == '-':
                operators.append(s[i])
            elif s[i] == '(':
                while operators[-1] != ')':
                    self.compute(operands, operators)
                operators.pop()

        while operators:
            self.compute(operands, operators)

        return operands[-1]

    def compute(self, operands, operators):
        left, right = operands.pop(), operands.pop()
        op = operators.pop()
        if op == '+':
            operands.append(left + right)
        elif op == '-':
            operands.append(left - right)


if __name__ == "__main__":
    # s = "(1+(4+5+2)-3)+(6+8)"
    s= " 2 - 1 + 2 "
    print(Solution().calculate(s))
