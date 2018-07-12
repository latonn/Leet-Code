#

# Given two words (beginWord and endWord), and a dictionary's word list, find the length of shortest transformation
# sequence from beginWord to endWord, such that:
#
# Only one letter can be changed at a time.
# Each transformed word must exist in the word list. Note that beginWord is not a transformed word.
# Note:
#
# Return 0 if there is no such transformation sequence.
# All words have the same length.
# All words contain only lowercase alphabetic characters.
# You may assume no duplicates in the word list.
# You may assume beginWord and endWord are non-empty and are not the same.
#
# Example 1:
#
# Input:
# beginWord = "hit",
# endWord = "cog",
# wordList = ["hot","dot","dog","lot","log","cog"]
#
# Output: 5
#
# Explanation: As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
# return its length 5.
#
# Example 2:
#
# Input:
# beginWord = "hit"
# endWord = "cog"
# wordList = ["hot","dot","dog","lot","log"]
#
# Output: 0
#
# Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.


class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        # BFS
        wordList.extend(endWord)
        wordList = set(wordList)
        q = []
        q.append((beginWord, 1))
        while q:
            curr = q.pop(0)
            currWord, currlen = curr[0], curr[1]
            print(currWord)
            if currWord == endWord:
                return currlen
            for i in range(len(currWord)):
                prefix, postfix = currWord[:i], currWord[i+1:]
                for j in 'abcdefghijklmnopqrstuvwxyz':
                    if currWord[i] != j:
                        nextWord = prefix + j + postfix
                        if nextWord in wordList:
                            q.append((nextWord, currlen + 1))
                            wordList.remove(nextWord)
        return 0


if __name__ == '__main__':
    beginWord = 'hit'
    endWord = 'cog'
    wordList = ['hot', 'dot', 'dog', 'lot', 'log', 'cog']
    print(Solution().ladderLength(beginWord, endWord, wordList))

