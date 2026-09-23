"""
LeetCode 304: Range Sum Query 2D - Immutable

Given a 2D matrix matrix, handle multiple queries of the following type:

- Calculate the sum of the elements of matrix inside the rectangle defined by its upper
  left corner (row1, col1) and lower right corner (row2, col2).

Implement the NumMatrix class:

- NumMatrix(int[][] matrix) Initializes the object with the integer matrix matrix.
- int sumRegion(int row1, int col1, int row2, int col2) Returns the sum of the elements
  of matrix inside the rectangle defined by its upper left corner (row1, col1) and lower
  right corner (row2, col2).

You must design an algorithm where sumRegion works on O(1) time complexity.

Example:
Input: ["NumMatrix", "sumRegion", "sumRegion", "sumRegion"]
       [[[[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]], [2, 1, 4, 3], [1, 1, 2, 2], [1, 2, 2, 4]]
Output: [null, 8, 11, 12]
Explanation:
NumMatrix numMatrix = new NumMatrix([[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5],
[4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]);
numMatrix.sumRegion(2, 1, 4, 3); // return 8 (i.e sum of the red rectangle)
numMatrix.sumRegion(1, 1, 2, 2); // return 11 (i.e sum of the green rectangle)
numMatrix.sumRegion(1, 2, 2, 4); // return 12 (i.e sum of the blue rectangle)

Constraints:
- m == matrix.length
- n == matrix[i].length
- 1 <= m, n <= 200
- -10^4 <= matrix[i][j] <= 10^4
- 0 <= row1 <= row2 < m
- 0 <= col1 <= col2 < n
- At most 10^4 calls will be made to sumRegion.
"""


class NumMatrix:
    def __init__(self, matrix):
        """
        Initialize the object with the integer matrix.

        Args:
            matrix: List[List[int]] - 2D matrix

        Time Complexity: O(?)
        Space Complexity: O(?)
        """
        # TODO: Implement initialization
        pass

    def sumRegion(self, row1, col1, row2, col2):
        """
        Sum of the elements inside the rectangle (row1, col1) to (row2, col2).

        Args:
            row1: int - upper-left row
            col1: int - upper-left column
            row2: int - lower-right row
            col2: int - lower-right column

        Returns:
            int - rectangle sum

        Time Complexity: O(?)
        Space Complexity: O(?)
        """
        # TODO: Implement sumRegion
        pass


# Example usage (for testing locally)
if __name__ == "__main__":
    matrix = [[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]
    numMatrix = NumMatrix(matrix)
    print("sumRegion(2, 1, 4, 3):", numMatrix.sumRegion(2, 1, 4, 3))  # 8
    print("sumRegion(1, 1, 2, 2):", numMatrix.sumRegion(1, 1, 2, 2))  # 11
    print("sumRegion(1, 2, 2, 4):", numMatrix.sumRegion(1, 2, 2, 4))  # 12
