"""
LeetCode 212: Word Search II

Given an m x n board of characters and a list of strings words, return all words on the
board.

Each word must be constructed from letters of sequentially adjacent cells, where
adjacent cells are horizontally or vertically neighboring. The same letter cell may not
be used more than once in a word.

Example 1:
Input: board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], words = ["oath","pea","eat","rain"]
Output: ["eat","oath"]

Example 2:
Input: board = [["a","b"],["c","d"]], words = ["abcb"]
Output: []

Constraints:
- m == board.length
- n == board[i].length
- 1 <= m, n <= 12
- board[i][j] is a lowercase English letter.
- 1 <= words.length <= 3 * 10^4
- 1 <= words[i].length <= 10
- words[i] consists of lowercase English letters.
- All the strings of words are unique.
"""


class Solution:
    def findWords(self, board, words):
        """
        Find all dictionary words that can be built on the board.

        Args:
            board: List[List[str]] - m x n grid of characters
            words: List[str] - words to find

        Returns:
            List[str] - found words in any order

        Time Complexity: O(?)
        Space Complexity: O(?)
        """
        # TODO: Implement solution
        pass


# Example usage (for testing locally)
if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    board = [["o", "a", "a", "n"], ["e", "t", "a", "e"], ["i", "h", "k", "r"], ["i", "f", "l", "v"]]
    result = solution.findWords(board, ["oath", "pea", "eat", "rain"])
    print(f"Test 1: {result}")

    # Test case 2
    result = solution.findWords([["a", "b"], ["c", "d"]], ["abcb"])
    print(f"Test 2: {result}")
