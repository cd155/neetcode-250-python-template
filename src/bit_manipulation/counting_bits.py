"""
LeetCode 338: Counting Bits

Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <=
n), ans[i] is the number of 1's in the binary representation of i.

Do not solve it with built-in functions (i.e., like __builtin_popcount in C++).

Example 1:
Input: n = 2
Output: [0,1,1]
Explanation:
0 --> 0
1 --> 1
2 --> 10

Example 2:
Input: n = 5
Output: [0,1,1,2,1,2]
Explanation:
0 --> 0
1 --> 1
2 --> 10
3 --> 11
4 --> 100
5 --> 101

Constraints:
- 0 <= n <= 10^5
- It is very easy to come up with a solution with a runtime of O(n log n). Can you do it
  in linear time O(n) and possibly in a single pass?

Follow up:
"""


class Solution:
    def countBits(self, n):
        """
        Count the 1 bits of every number from 0 to n.

        Args:
            n: int - integer n

        Returns:
            List[int] - ans[i] is the number of 1 bits in i

        Time Complexity: O(?)
        Space Complexity: O(?)
        """
        # TODO: Implement solution
        pass


# Example usage (for testing locally)
if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    result = solution.countBits(2)
    print(f"Test 1: {result}")

    # Test case 2
    result = solution.countBits(5)
    print(f"Test 2: {result}")
