"""
LeetCode 64: Minimum Path Sum

Given a m x n grid filled with non-negative numbers, find a path from top left to bottom
right, which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

Example 1:
Input: grid = [[1,3,1],[1,5,1],[4,2,1]]
Output: 7
Explanation: Because the path 1 -> 3 -> 1 -> 1 -> 1 minimizes the sum.

Example 2:
Input: grid = [[1,2,3],[4,5,6]]
Output: 12

Constraints:
- m == grid.length
- n == grid[i].length
- 1 <= m, n <= 200
- 0 <= grid[i][j] <= 200
"""


class Solution:
    def minPathSum(self, grid):
        """
        Minimum path sum from the top-left to the bottom-right corner.

        Args:
            grid: List[List[int]] - m x n grid of non-negative numbers

        Returns:
            int - minimum path sum

        Time Complexity: O(?)
        Space Complexity: O(?)
        """
        # TODO: Implement solution
        pass


# Example usage (for testing locally)
if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    result = solution.minPathSum([[1, 3, 1], [1, 5, 1], [4, 2, 1]])
    print(f"Test 1: {result}")

    # Test case 2
    result = solution.minPathSum([[1, 2, 3], [4, 5, 6]])
    print(f"Test 2: {result}")
