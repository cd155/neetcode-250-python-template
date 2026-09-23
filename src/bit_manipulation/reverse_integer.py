"""
LeetCode 7: Reverse Integer

Given a signed 32-bit integer x, return x with its digits reversed. If reversing x
causes the value to go outside the signed 32-bit integer range [-2^31, 2^31 - 1], then
return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

Example 1:
Input: x = 123
Output: 321

Example 2:
Input: x = -123
Output: -321

Example 3:
Input: x = 120
Output: 21

Constraints:
- -2^31 <= x <= 2^31 - 1
"""


class Solution:
    def reverse(self, x):
        """
        Reverse the digits of a signed 32-bit integer.

        Args:
            x: int - signed 32-bit integer

        Returns:
            int - reversed integer, or 0 on overflow

        Time Complexity: O(?)
        Space Complexity: O(?)
        """
        # TODO: Implement solution
        pass


# Example usage (for testing locally)
if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    result = solution.reverse(123)
    print(f"Test 1: {result}")

    # Test case 2
    result = solution.reverse(-123)
    print(f"Test 2: {result}")
