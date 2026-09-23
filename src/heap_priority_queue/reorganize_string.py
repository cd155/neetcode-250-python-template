"""
LeetCode 767: Reorganize String

Given a string s, rearrange the characters of s so that any two adjacent characters are
not the same.

Return any possible rearrangement of s or return "" if not possible.

Example 1:
Input: s = "aab"
Output: "aba"

Example 2:
Input: s = "aaab"
Output: ""

Constraints:
- 1 <= s.length <= 500
- s consists of lowercase English letters.
"""


class Solution:
    def reorganizeString(self, s):
        """
        Rearrange s so that no two adjacent characters are the same.

        Args:
            s: str - input string

        Returns:
            str - any valid rearrangement, or an empty string

        Time Complexity: O(?)
        Space Complexity: O(?)
        """
        # TODO: Implement solution
        pass


# Example usage (for testing locally)
if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    result = solution.reorganizeString("aab")
    print(f"Test 1: {result!r}")

    # Test case 2
    result = solution.reorganizeString("aaab")
    print(f"Test 2: {result!r}")
