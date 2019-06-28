#

# Given a list of unique words, find all pairs of distinct indices (i, j) in the given list, so that the concatenation
# of the two words, i.e. words[i] + words[j] is a palindrome.
#
# Example 1:
# Input: ["abcd","dcba","lls","s","sssll"]
# Output: [[0,1],[1,0],[3,2],[2,4]]
# Explanation: The palindromes are ["dcbaabcd","abcddcba","slls","llssssll"]
#
# Example 2:
# Input: ["bat","tab","cat"]
# Output: [[0,1],[1,0]]
# Explanation: The palindromes are ["battab","tabbat"]


class Solution(object):
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        # refer from http://bookshadow.com/weblog/2016/03/10/leetcode-palindrome-pairs/
        wordmap = {word: i for i, word in enumerate(words)}

        def isPalindrome(word):
            size = len(word)
            for i in range(int(size/2)):
                if word[i] != word[size - i - 1]:
                    return False
            return True

        ans = set()
        for idx, word in enumerate(words):
            # the word is palindromic itself
            if "" in wordmap and word != "" and isPalindrome(word):
                bidx = wordmap[""]
                ans.add((bidx, idx))
                ans.add((idx, bidx))

            # check if there were a reverse of the word
            rword = word[::-1]
            if rword in wordmap:
                ridx = wordmap[rword]
                if idx != ridx:
                    ans.add((idx, ridx))
                    ans.add((ridx, idx))

            # partial of the word is palindromic, partial is not
            for x in range(1, len(word)):
                left, right = word[:x], word[x:]
                rleft, rright = left[::-1], right[::-1]
                if isPalindrome(left) and rright in wordmap:
                    ans.add((wordmap[rright], idx))
                if isPalindrome(right) and rleft in wordmap:
                    ans.add((idx, wordmap[rleft]))
        return list(ans)


if __name__ == "__main__":
    words = ["abcd", "dcba", "lls", "s", "sssll"]
    print(Solution().palindromePairs(words))

