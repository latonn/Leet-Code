# Time:  O(n)
# Space: O(k), k is size of the alphabet

# Given a string which contains only lowercase letters, remove duplicate letters so that every letter appear once and
# only once. You must make sure your result is the smallest in lexicographical order among all possible results.
#
# Example 1:
#
# Input: "bcabc"
# Output: "abc"
#
# Example 2:
#
# Input: "cbacdcbc"
# Output: "acdb"


class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        from collections import defaultdict
        lettercount = defaultdict(int)
        result = set()
        stack = []
        for c in s:
            lettercount[c] += 1

        for c in s:
            lettercount[c] -= 1
            if c in result:
                continue

            while stack and stack[-1] > c and lettercount[stack[-1]]:
                result.remove(stack.pop())
            result.add(c)
            stack.append(c)

        return ''.join(stack)


if __name__ == '__main__':
    s = 'cbacdcbc'
    print(Solution().removeDuplicateLetters(s))
