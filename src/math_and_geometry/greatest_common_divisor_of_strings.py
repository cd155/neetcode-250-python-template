"""
LeetCode 1071: Greatest Common Divisor of Strings

For two strings s and t, we say "t divides s" if and only if s = t + t + t + ... + t + t
(i.e., t is concatenated with itself one or more times).

Given two strings str1 and str2, return the largest string x such that x divides both
str1 and str2.

Example 1:
Input: str1 = "ABCABC", str2 = "ABC"
Output: "ABC"

Example 2:
Input: str1 = "ABABAB", str2 = "ABAB"
Output: "AB"

Example 3:
Input: str1 = "LEET", str2 = "CODE"
Output: ""

Example 4:
Input: str1 = "AAAAAB", str2 = "AAA"
Output: ""

Constraints:
- 1 <= str1.length, str2.length <= 1000
- str1 and str2 consist of English uppercase letters.
"""


class Solution:
    def gcdOfStrings(self, str1, str2):
        """
        Largest string x that divides both str1 and str2.

        Args:
            str1: str - first string
            str2: str - second string

        Returns:
            str - largest common divisor string, or an empty string

        Time Complexity: O(?)
        Space Complexity: O(?)
        """
        # TODO: Implement solution
        pass


# Example usage (for testing locally)
if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    result = solution.gcdOfStrings("ABCABC", "ABC")
    print(f"Test 1: {result!r}")

    # Test case 2
    result = solution.gcdOfStrings("ABABAB", "ABAB")
    print(f"Test 2: {result!r}")
