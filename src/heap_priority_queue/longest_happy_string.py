"""
LeetCode 1405: Longest Happy String

A string s is called happy if it satisfies the following conditions:

- s only contains the letters 'a', 'b', and 'c'.
- s does not contain any of "aaa", "bbb", or "ccc" as a substring.
- s contains at most a occurrences of the letter 'a'.
- s contains at most b occurrences of the letter 'b'.
- s contains at most c occurrences of the letter 'c'.

Given three integers a, b, and c, return the longest possible happy string. If there are
multiple longest happy strings, return any of them. If there is no such string, return
the empty string "".

A substring is a contiguous sequence of characters within a string.

Example 1:
Input: a = 1, b = 1, c = 7
Output: "ccaccbcc"
Explanation: "ccbccacc" would also be a correct answer.

Example 2:
Input: a = 7, b = 1, c = 0
Output: "aabaa"
Explanation: It is the only correct answer in this case.

Constraints:
- 0 <= a, b, c <= 100
- a + b + c > 0
"""


class Solution:
    def longestDiverseString(self, a, b, c):
        """
        Build the longest string without 'aaa', 'bbb' or 'ccc'.

        Args:
            a: int - maximum number of 'a'
            b: int - maximum number of 'b'
            c: int - maximum number of 'c'

        Returns:
            str - any longest happy string

        Time Complexity: O(?)
        Space Complexity: O(?)
        """
        # TODO: Implement solution
        pass


# Example usage (for testing locally)
if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    result = solution.longestDiverseString(1, 1, 7)
    print(f"Test 1: {result!r}")

    # Test case 2
    result = solution.longestDiverseString(7, 1, 0)
    print(f"Test 2: {result!r}")
