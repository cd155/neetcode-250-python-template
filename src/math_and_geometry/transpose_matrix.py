"""
LeetCode 867: Transpose Matrix

Given a 2D integer array matrix, return the transpose of matrix.

The transpose of a matrix is the matrix flipped over its main diagonal, switching the
matrix's row and column indices.

Example 1:
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[1,4,7],[2,5,8],[3,6,9]]

Example 2:
Input: matrix = [[1,2,3],[4,5,6]]
Output: [[1,4],[2,5],[3,6]]

Constraints:
- m == matrix.length
- n == matrix[i].length
- 1 <= m, n <= 1000
- 1 <= m * n <= 10^5
- -10^9 <= matrix[i][j] <= 10^9
"""


class Solution:
    def transpose(self, matrix):
        """
        Return the transpose of the matrix.

        Args:
            matrix: List[List[int]] - 2D matrix

        Returns:
            List[List[int]] - transposed matrix

        Time Complexity: O(?)
        Space Complexity: O(?)
        """
        # TODO: Implement solution
        pass


# Example usage (for testing locally)
if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    result = solution.transpose([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    print(f"Test 1: {result}")

    # Test case 2
    result = solution.transpose([[1, 2, 3], [4, 5, 6]])
    print(f"Test 2: {result}")
