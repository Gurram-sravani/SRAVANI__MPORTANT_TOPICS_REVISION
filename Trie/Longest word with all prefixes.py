from typing import List

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False


class Trie:
    def __init__(self):
        self.root = TrieNode()   # must be an object, not the class

    def insert(self, word):      # insert ONE word, not (root, words)
        curr = self.root
        for ch in word:          # word is a string -> iterates characters
            if ch not in curr.children:
                curr.children[ch] = TrieNode()   # create next node
            curr = curr.children[ch]             # move forward
        curr.is_end = True

    def backtrack(self, node, path):
        """
        Returns best word from this node downward.
        Only moves to children that are is_end=True (valid prefix rule).
        """
        best = "".join(path)  # current word formed so far

        for ch in sorted(node.children.keys()):     # sorted helps lexicographic tie
            nxt = node.children[ch]
            if nxt.is_end:                          # prefix must be a word
                path.append(ch)
                candidate = self.backtrack(nxt, path)
                path.pop()

                # choose longer; if tie, lexicographically smaller
                if len(candidate) > len(best) or (len(candidate) == len(best) and candidate < best):
                    best = candidate

        return best


class Solution:
    def longestWord(self, words: List[str]) -> str:
        trie = Trie()
        for word in words:
            trie.insert(word)

        # start DFS from root with empty path
        return trie.backtrack(trie.root, [])

# Time complexity: O(N * L)
# Space complexity :  Space = O(N * L)
