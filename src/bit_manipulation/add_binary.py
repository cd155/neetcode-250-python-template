"""
LeetCode 67: Add Binary

Given two binary strings a and b, return their sum as a binary string.

Example 1:
Input: a = "11", b = "1"
Output: "100"

Example 2:
Input: a = "1010", b = "1011"
Output: "10101"

Constraints:
- 1 <= a.length, b.length <= 10^4
- a and b consist only of '0' or '1' characters.
- Each string does not contain leading zeros except for the zero itself.
"""


class Solution:
    def addBinary(self, a, b):
        """
        Add two binary strings.

        Args:
            a: str - binary string
            b: str - binary string

        Returns:
            str - sum as a binary string

        Time Complexity: O(?)
        Space Complexity: O(?)
        """
        # TODO: Implement solution
        pass


# Example usage (for testing locally)
if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    result = solution.addBinary("11", "1")
    print(f"Test 1: {result!r}")

    # Test case 2
    result = solution.addBinary("1010", "1011")
    print(f"Test 2: {result!r}")
