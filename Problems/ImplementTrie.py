# https://leetcode.com/explore/challenge/card/may-leetcoding-challenge/535/week-2-may-8th-may-14th/3329/

class TrieNode():
    def __init__(self):
        self.children = {}
        self.end_of_word = False


class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: None
        """
        curr_node = self.root
        for letter in word:
            node = curr_node.children.get(letter)
            # We don't have this letter in the current node's dict yet
            if not node:
                node = TrieNode()
                curr_node.children[letter] = node
            curr_node = node
        curr_node.end_of_word = True

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        curr_node = self.root
        for letter in word:
            node = curr_node.children.get(letter)
            # We don't have this letter in the node
            if not node:
                return False
            curr_node = node
        return curr_node.end_of_word

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        curr_node = self.root
        for letter in prefix:
            node = curr_node.children.get(letter)
            if not node:
                return False
            curr_node = node
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)