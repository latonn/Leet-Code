#

# Write a function to generate the generalized abbreviations of a word.
#
# Note: The order of the output does not matter.
#
# Example:
#
# Input: "word"
# Output:
# ["word", "1ord", "w1rd", "wo1d", "wor1", "2rd", "w2d", "wo2", "1o1d", "1or1", "w1r1", "1o2", "2r1", "3d", "w3", "4"]


class Solution(object):
    def generateAbbreviations(self, word):
        """
        :type word: str
        :rtype: List[str]
        """
        # latonn's
        # Backtracking
        def backTrack(word, i, seq, result):
            if i == len(word):
                result.append(seq)
                return
            for j in range(i, len(word)):
                num = str(j - i) if j - i > 0 else ''
                backTrack(word, j+1, seq + num + word[j], result)
            backTrack(word, len(word), seq + str(len(word) - i), result)

        result = []
        backTrack(word, 0, '', result)
        return result


if __name__ == '__main__':
    word = 'word'
    print(Solution().generateAbbreviations(word))

