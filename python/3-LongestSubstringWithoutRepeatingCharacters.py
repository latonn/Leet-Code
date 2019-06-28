# Time:  O(n)
# Space: O(1)

# Given a string, find the length of the longest substring without repeating characters.
#
# Examples:
#
# Given "abcabcbb", the answer is "abc", which the length is 3.
#
# Given "bbbbb", the answer is "b", with the length of 1.
#
# Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be
# a substring, "pwke" is a subsequence and not a substring.


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # latonn's
        longest, begin, record = 0, 0, {}
        for i, char in enumerate(s):
            if char in record.keys():
                begin = max(begin, record[char] + 1)
                record[char] = i
            else:
                record.setdefault(char, i)
            longest = max(longest, i - begin + 1)
        return longest

        # kamyu's
        # longest, start, visited = 0, 0, [False for _ in range(256)]
        # for i, char in enumerate(s):
        #     if visited[ord(char)]:
        #         while char != s[start]:
        #             visited[ord(s[start])] = False
        #             start += 1
        #         start += 1
        #     else:
        #         visited[ord(char)] = True
        #     longest = max(longest, i - start + 1)
        # return longest


if __name__ == '__main__':
    s = "abcabcbb"
    print("Ans: ", Solution().lengthOfLongestSubstring(s))

