"""
LeetCode 50: Pow(x, n)

Implement pow(x, n), which calculates x raised to the power n (i.e., x^n).

Example 1:
Input: x = 2.00000, n = 10
Output: 1024.00000

Example 2:
Input: x = 2.10000, n = 3
Output: 9.26100

Example 3:
Input: x = 2.00000, n = -2
Output: 0.25000
Explanation: 2^-2 = 1/2^2 = 1/4 = 0.25

Constraints:
- -100.0 < x < 100.0
- -2^31 <= n <= 2^31-1
- n is an integer.
- Either x is not zero or n > 0.
- -10^4 <= x^n <= 10^4
"""


class Solution:
    def myPow(self, x, n):
        """
        Compute x raised to the power n.

        Args:
            x: float - base
            n: int - exponent

        Returns:
            float - x^n

        Time Complexity: O(?)
        Space Complexity: O(?)
        """
        # TODO: Implement solution
        pass


# Example usage (for testing locally)
if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    result = solution.myPow(2.0, 10)
    print(f"Test 1: {result}")

    # Test case 2
    result = solution.myPow(2.1, 3)
    print(f"Test 2: {result}")
