#

# Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also
# represented as a string.
#
# Example 1:
# Input: num1 = "2", num2 = "3"
# Output: "6"
#
# Example 2:
# Input: num1 = "123", num2 = "456"
# Output: "56088"
#
# Note:
# The length of both num1 and num2 is < 110.
# Both num1 and num2 contain only digits 0-9.
# Both num1 and num2 do not contain any leading zero, except the number 0 itself.
# You must not use any built-in BigInteger library or convert the inputs to integer directly.


class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        num1, num2 = num1[::-1], num2[::-1]
        # print(num1, num2)
        result = [0 for _ in range(len(num1) + len(num2))]
        for i in range(len(num1)):
            for j in range(len(num2)):
                result[i+j] += int(num1[i]) * int(num2[j])

        ans = []
        for k in range(len(result)):
            sum = int(result[k] % 10)
            carry = int(result[k] / 10)
            if k < len(result) - 1:
                result[k+1] += carry
            ans.insert(0, str(sum))

        while ans[0] == '0' and len(ans) > 1:
            del ans[0]

        # print(result)
        return ''.join(ans)


if __name__ == '__main__':
    num1 = '123'
    num2 = '456'
    print(Solution().multiply(num1, num2))
