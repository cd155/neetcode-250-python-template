"""
LeetCode 69: Sqrt(x)

Given a non-negative integer x, return the square root of x rounded down to the nearest
integer. The returned integer should be non-negative as well.

You must not use any built-in exponent function or operator.

- For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.

Example 1:
Input: x = 4
Output: 2
Explanation: The square root of 4 is 2, so we return 2.

Example 2:
Input: x = 8
Output: 2
Explanation:
The square root of 8 is 2.82842..., and since we round it down to the nearest integer, 2
is returned.

Constraints:
- 0 <= x <= 2^31 - 1
"""


class Solution:
    def mySqrt(self, x):
        """
        Compute the square root of x rounded down, without built-in exponent functions.

        Args:
            x: int - non-negative integer

        Returns:
            int - square root of x rounded down

        Time Complexity: O(?)
        Space Complexity: O(?)
        """
        # TODO: Implement solution
        pass


# Example usage (for testing locally)
if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    result = solution.mySqrt(4)
    print(f"Test 1: {result}")

    # Test case 2
    result = solution.mySqrt(8)
    print(f"Test 2: {result}")
