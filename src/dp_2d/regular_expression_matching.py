"""
LeetCode 10: Regular Expression Matching

Given an input string s and a pattern p, implement regular expression matching with
support for '.' and '*' where:

- '.' Matches any single character.
- '*' Matches zero or more of the preceding element.

Return a boolean indicating whether the matching covers the entire input string (not
partial).

Example 1:
Input: s = "aa", p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".

Example 2:
Input: s = "aa", p = "a*"
Output: true
Explanation:
'*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once,
it becomes "aa".

Example 3:
Input: s = "ab", p = ".*"
Output: true
Explanation: ".*" means "zero or more (*) of any character (.)".

Constraints:
- 1 <= s.length <= 20
- 1 <= p.length <= 20
- s contains only lowercase English letters.
- p contains only lowercase English letters, '.', and '*'.
- It is guaranteed for each appearance of the character '*', there will be a previous
  valid character to match.
"""


class Solution:
    def isMatch(self, s, p):
        """
        Regular expression matching with support for '.' and '*'.

        Args:
            s: str - input string
            p: str - pattern

        Returns:
            bool - True if p matches the entire string s

        Time Complexity: O(?)
        Space Complexity: O(?)
        """
        # TODO: Implement solution
        pass


# Example usage (for testing locally)
if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    result = solution.isMatch("aa", "a")
    print(f"Test 1: {result}")

    # Test case 2
    result = solution.isMatch("aa", "a*")
    print(f"Test 2: {result}")
