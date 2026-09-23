"""
LeetCode 190: Reverse Bits

Reverse bits of a given 32 bits signed integer.

Example 1:
Input: n = 43261596
Output: 964176192
Explanation:
Integer | Binary
43261596 | 00000010100101000001111010011100
964176192 | 00111001011110000010100101000000

Example 2:
Input: n = 2147483644
Output: 1073741822
Explanation:
Integer | Binary
2147483644 | 01111111111111111111111111111100
1073741822 | 00111111111111111111111111111110

Constraints:
- 0 <= n <= 2^31 - 2
- n is even.

Follow up: If this function is called many times, how would you optimize it?
"""


class Solution:
    def reverseBits(self, n):
        """
        Reverse the bits of a 32-bit unsigned integer.

        Args:
            n: int - 32-bit unsigned integer

        Returns:
            int - integer with the bits reversed

        Time Complexity: O(?)
        Space Complexity: O(?)
        """
        # TODO: Implement solution
        pass


# Example usage (for testing locally)
if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    result = solution.reverseBits(43261596)
    print(f"Test 1: {result}")

    # Test case 2
    result = solution.reverseBits(2147483644)
    print(f"Test 2: {result}")
