"""
LeetCode 208: Implement Trie (Prefix Tree)

A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently
store and retrieve keys in a dataset of strings. There are various applications of this
data structure, such as autocomplete and spellchecker.

Implement the Trie class:

- Trie() Initializes the trie object.
- void insert(String word) Inserts the string word into the trie.
- boolean search(String word) Returns true if the string word is in the trie (i.e., was
  inserted before), and false otherwise.
- boolean startsWith(String prefix) Returns true if there is a previously inserted
  string word that has the prefix prefix, and false otherwise.

Example:
Input: ["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
       [[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
Output: [null, null, true, false, true, null, true]
Explanation:
Trie trie = new Trie();
trie.insert("apple");
trie.search("apple");   // return True
trie.search("app");     // return False
trie.startsWith("app"); // return True
trie.insert("app");
trie.search("app");     // return True

Constraints:
- 1 <= word.length, prefix.length <= 2000
- word and prefix consist only of lowercase English letters.
- At most 3 * 10^4 calls in total will be made to insert, search, and startsWith.
"""


class Trie:
    def __init__(self):
        """
        Initialize the trie.

        Time Complexity: O(?)
        Space Complexity: O(?)
        """
        # TODO: Implement initialization
        pass

    def insert(self, word):
        """
        Insert word into the trie.

        Args:
            word: str - word

        Time Complexity: O(?)
        Space Complexity: O(?)
        """
        # TODO: Implement insert
        pass

    def search(self, word):
        """
        Check whether word was inserted before.

        Args:
            word: str - word

        Returns:
            bool - True if word is in the trie

        Time Complexity: O(?)
        Space Complexity: O(?)
        """
        # TODO: Implement search
        pass

    def startsWith(self, prefix):
        """
        Check whether any inserted word starts with prefix.

        Args:
            prefix: str - prefix

        Returns:
            bool - True if some word has the prefix

        Time Complexity: O(?)
        Space Complexity: O(?)
        """
        # TODO: Implement startsWith
        pass


# Example usage (for testing locally)
if __name__ == "__main__":
    trie = Trie()
    trie.insert("apple")
    print("search('apple'):", trie.search("apple"))  # True
    print("search('app'):", trie.search("app"))  # False
    print("startsWith('app'):", trie.startsWith("app"))  # True
    trie.insert("app")
    print("search('app'):", trie.search("app"))  # True
