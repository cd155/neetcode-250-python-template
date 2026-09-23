"""
LeetCode 680: Valid Palindrome II

Given a string s, return true if the s can be palindrome after deleting at most one
character from it.

Example 1:
Input: s = "aba"
Output: true

Example 2:
Input: s = "abca"
Output: true
Explanation: You could delete the character 'c'.

Example 3:
Input: s = "abc"
Output: false

Constraints:
- 1 <= s.length <= 10^5
- s consists of lowercase English letters.
"""


class Solution:
    def validPalindrome(self, s):
        """
        Check whether s can be a palindrome after deleting at most one character.

        Args:
            s: str - input string

        Returns:
            bool - True if s can be a palindrome

        Time Complexity: O(?)
        Space Complexity: O(?)
        """
        # TODO: Implement solution
        pass


# Example usage (for testing locally)
if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    result = solution.validPalindrome("aba")
    print(f"Test 1: {result}")

    # Test case 2
    result = solution.validPalindrome("abca")
    print(f"Test 2: {result}")
