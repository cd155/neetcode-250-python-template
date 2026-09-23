"""
LeetCode 168: Excel Sheet Column Title

Given an integer columnNumber, return its corresponding column title as it appears in an
Excel sheet.

For example:

A -> 1
B -> 2
C -> 3
...
Z -> 26
AA -> 27
AB -> 28
...

Example 1:
Input: columnNumber = 1
Output: "A"

Example 2:
Input: columnNumber = 28
Output: "AB"

Example 3:
Input: columnNumber = 701
Output: "ZY"

Constraints:
- 1 <= columnNumber <= 2^31 - 1
"""


class Solution:
    def convertToTitle(self, columnNumber):
        """
        Convert a column number to its Excel column title.

        Args:
            columnNumber: int - column number

        Returns:
            str - column title

        Time Complexity: O(?)
        Space Complexity: O(?)
        """
        # TODO: Implement solution
        pass


# Example usage (for testing locally)
if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    result = solution.convertToTitle(1)
    print(f"Test 1: {result!r}")

    # Test case 2
    result = solution.convertToTitle(28)
    print(f"Test 2: {result!r}")
