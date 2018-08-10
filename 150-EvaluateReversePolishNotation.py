#

# Evaluate the value of an arithmetic expression in Reverse Polish Notation.
#
# Valid operators are +, -, *, /. Each operand may be an integer or another expression.
#
# Note:
#
# Division between two integers should truncate toward zero.
# The given RPN expression is always valid. That means the expression would always evaluate to a result and there won't
# be any divide by zero operation.
# Example 1:
#
# Input: ["2", "1", "+", "3", "*"]
# Output: 9
# Explanation: ((2 + 1) * 3) = 9
# Example 2:
#
# Input: ["4", "13", "5", "/", "+"]
# Output: 6
# Explanation: (4 + (13 / 5)) = 6
# Example 3:
#
# Input: ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
# Output: 22
# Explanation:
#   ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
# = ((10 * (6 / (12 * -11))) + 17) + 5
# = ((10 * (6 / -132)) + 17) + 5
# = ((10 * 0) + 17) + 5
# = (0 + 17) + 5
# = 17 + 5
# = 22


class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        # latonn's
        operand = []
        for token in tokens:
            if token not in ["+", "-", "*", "/"]:
                operand.append(int(token))
            else:
                operand2, operand1 = operand.pop(), operand.pop()
                if token == "+":
                    operand.append(operand1 + operand2)
                elif token == "-":
                    operand.append(operand1 - operand2)
                elif token == "*":
                    operand.append(operand1 * operand2)
                else:
                    operand.append(int(operand1 / operand2))
            # print(operand)
        return operand[0]

        # kamyu's
        # import operator
        # numerals, operators = [], {"+": operator.add, "-": operator.sub, "*": operator.mul, "/": operator.div}
        # for token in tokens:
        #     if token not in operators:
        #         numerals.append(int(token))
        #     else:
        #         y, x = numerals.pop(), numerals.pop()
        #         numerals.append(int(operators[token](x * 1.0, y)))
        # return numerals.pop()


if __name__ == "__main__":
    tokens = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
    print(Solution().evalRPN(tokens))
