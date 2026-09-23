"""
LeetCode 43: Multiply Strings

Given two non-negative integers num1 and num2 represented as strings, return the product
of num1 and num2, also represented as a string.

Note: You must not use any built-in BigInteger library or convert the inputs to integer
directly.

Example 1:
Input: num1 = "2", num2 = "3"
Output: "6"

Example 2:
Input: num1 = "123", num2 = "456"
Output: "56088"

Constraints:
- 1 <= num1.length, num2.length <= 200
- num1 and num2 consist of digits only.
- Both num1 and num2 do not contain any leading zero, except the number 0 itself.
"""


class Solution:
    def multiply(self, num1, num2):
        """
        Multiply two non-negative integers given as strings.

        Args:
            num1: str - first non-negative integer as a string
            num2: str - second non-negative integer as a string

        Returns:
            str - product as a string

        Time Complexity: O(?)
        Space Complexity: O(?)
        """
        # TODO: Implement solution
        pass


# Example usage (for testing locally)
if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    result = solution.multiply("2", "3")
    print(f"Test 1: {result!r}")

    # Test case 2
    result = solution.multiply("123", "456")
    print(f"Test 2: {result!r}")
