"""
LeetCode 51: N-Queens

The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that
no two queens attack each other.

Given an integer n, return all distinct solutions to the n-queens puzzle. You may return
the answer in any order.

Each solution contains a distinct board configuration of the n-queens' placement, where
'Q' and '.' both indicate a queen and an empty space, respectively.

Example 1:
Input: n = 4
Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above

Example 2:
Input: n = 1
Output: [["Q"]]

Constraints:
- 1 <= n <= 9
"""


class Solution:
    def solveNQueens(self, n):
        """
        Return all distinct solutions to the n-queens puzzle.

        Args:
            n: int - board size and number of queens

        Returns:
            List[List[str]] - all board configurations in any order

        Time Complexity: O(?)
        Space Complexity: O(?)
        """
        # TODO: Implement solution
        pass


# Example usage (for testing locally)
if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    result = solution.solveNQueens(4)
    print(f"Test 1: {result}")

    # Test case 2
    result = solution.solveNQueens(1)
    print(f"Test 2: {result}")
