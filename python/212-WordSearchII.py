#

# Given a 2D board and a list of words from the dictionary, find all words in the board.
#
# Each word must be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those
# horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.
#
# Example:
#
# Input:
# words = ["oath","pea","eat","rain"] and board =
# [
#   ['o','a','a','n'],
#   ['e','t','a','e'],
#   ['i','h','k','r'],
#   ['i','f','l','v']
# ]
#
# Output: ["eat","oath"]
#
# Note:
# You may assume that all inputs are consist of lowercase letters a-z.


class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        result = []
        tree = Trie()
        visited = [[False] * len(board[0]) for _ in range(len(board))]
        for i in range(len(words)):
            tree.TrieInsert(words[i])

        def dfs(word, root, i, j):
            root = root.childs.get(board[i][j])
            if not root:
                return
            visited[i][j] = True
            for di, dj in zip((1, 0, -1, 0), (0, 1, 0, -1)):
                i_n, j_n = i + di, j + dj
                if i_n < 0 or j_n < 0 or i_n > len(board) - 1 or j_n > len(board[0]) - 1 or visited[i_n][j_n]:
                    continue
                dfs(word + board[i_n][j_n], root, i_n, j_n)
            if root.isWord:
                result.append(word)
                tree.TrieDelete(word)
            visited[i][j] = False

        for i in range(len(board)):
            for j in range(len(board[0])):
                dfs(board[i][j], tree.root, i, j)
        return result


class TrieNode(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.childs = {}
        self.isWord = False


class Trie(object):
    def __init__(self):
        self.root = TrieNode()

    def TrieInsert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        node = self.root
        for i in range(len(word)):
            if word[i] in node.childs:
                node = node.childs[word[i]]
            else:
                node.childs[word[i]] = TrieNode()
                node = node.childs[word[i]]
        node.isWord = True

    def TrieDelete(self, word):
        node = self.root
        stack = []
        for i in range(len(word)):
            stack.append([node, word[i]])
            node = node.childs[word[i]]
            if node is None:
                return False
        if not node.isWord:
            return False
        elif node.childs:
            node.isWord = False
            return True
        else:
            while stack:
                dnode, string = stack.pop()
                del dnode.childs[string]
                if len(dnode.childs) or dnode.isWord:
                    break

            return True


if __name__ == '__main__':
    board = [['o', 'a', 'a', 'n'],
             ['e', 't', 'a', 'e'],
             ['i', 'h', 'k', 'r'],
             ['i', 'f', 'l', 'v']]
    words = ["oath", "pea", "eat", "rain"]
    print(Solution().findWords(board, words))

