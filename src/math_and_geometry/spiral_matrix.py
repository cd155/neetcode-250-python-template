"""
LeetCode 54: Spiral Matrix

Given an m x n matrix, return all elements of the matrix in spiral order.

Example 1:
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]

Example 2:
Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]

Constraints:
- m == matrix.length
- n == matrix[i].length
- 1 <= m, n <= 10
- -100 <= matrix[i][j] <= 100
"""


class Solution:
    def spiralOrder(self, matrix):
        """
        Return all elements of the matrix in spiral order.

        Args:
            matrix: List[List[int]] - 2D matrix

        Returns:
            List[int] - elements in spiral order

        Time Complexity: O(?)
        Space Complexity: O(?)
        """
        # TODO: Implement solution
        pass


# Example usage (for testing locally)
if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    result = solution.spiralOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    print(f"Test 1: {result}")

    # Test case 2
    matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    result = solution.spiralOrder(matrix)
    print(f"Test 2: {result}")
