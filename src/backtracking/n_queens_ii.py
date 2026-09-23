"""
LeetCode 52: N-Queens II

The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that
no two queens attack each other.

Given an integer n, return the number of distinct solutions to the n-queens puzzle.

Example 1:
Input: n = 4
Output: 2
Explanation: There are two distinct solutions to the 4-queens puzzle as shown.

Example 2:
Input: n = 1
Output: 1

Constraints:
- 1 <= n <= 9
"""


class Solution:
    def totalNQueens(self, n):
        """
        Count the distinct solutions to the n-queens puzzle.

        Args:
            n: int - board size and number of queens

        Returns:
            int - number of solutions

        Time Complexity: O(?)
        Space Complexity: O(?)
        """
        # TODO: Implement solution
        pass


# Example usage (for testing locally)
if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    result = solution.totalNQueens(4)
    print(f"Test 1: {result}")

    # Test case 2
    result = solution.totalNQueens(1)
    print(f"Test 2: {result}")
