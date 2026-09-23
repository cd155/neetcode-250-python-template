"""
LeetCode 191: Number of 1 Bits

Given a positive integer n, write a function that returns the number of set bits in its
binary representation (also known as the Hamming weight).

Example 1:
Input: n = 11
Output: 3
Explanation: The input binary string 1011 has a total of three set bits.

Example 2:
Input: n = 128
Output: 1
Explanation: The input binary string 10000000 has a total of one set bit.

Example 3:
Input: n = 2147483645
Output: 30
Explanation:
The input binary string 1111111111111111111111111111101 has a total of thirty set bits.

Constraints:
- 1 <= n <= 2^31 - 1

Follow up: If this function is called many times, how would you optimize it?
"""


class Solution:
    def hammingWeight(self, n):
        """
        Count the set bits in the binary representation of n.

        Args:
            n: int - positive integer

        Returns:
            int - number of set bits

        Time Complexity: O(?)
        Space Complexity: O(?)
        """
        # TODO: Implement solution
        pass


# Example usage (for testing locally)
if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    result = solution.hammingWeight(11)
    print(f"Test 1: {result}")

    # Test case 2
    result = solution.hammingWeight(128)
    print(f"Test 2: {result}")
