"""
LeetCode 201: Bitwise AND of Numbers Range

Given two integers left and right that represent the range [left, right], return the
bitwise AND of all numbers in this range, inclusive.

Example 1:
Input: left = 5, right = 7
Output: 4

Example 2:
Input: left = 0, right = 0
Output: 0

Example 3:
Input: left = 1, right = 2147483647
Output: 0

Constraints:
- 0 <= left <= right <= 2^31 - 1
"""


class Solution:
    def rangeBitwiseAnd(self, left, right):
        """
        Bitwise AND of all numbers in [left, right].

        Args:
            left: int - range start
            right: int - range end

        Returns:
            int - bitwise AND of the range

        Time Complexity: O(?)
        Space Complexity: O(?)
        """
        # TODO: Implement solution
        pass


# Example usage (for testing locally)
if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    result = solution.rangeBitwiseAnd(5, 7)
    print(f"Test 1: {result}")

    # Test case 2
    result = solution.rangeBitwiseAnd(0, 0)
    print(f"Test 2: {result}")
