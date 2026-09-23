"""
LeetCode 242: Valid Anagram

Given two strings s and t, return true if t is an anagram of s, and false otherwise.

Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

Example 2:
Input: s = "rat", t = "car"
Output: false

Constraints:
- 1 <= s.length, t.length <= 5 * 10^4
- s and t consist of lowercase English letters.

Follow up: What if the inputs contain Unicode characters? How would you adapt your
solution to such a case?
"""


class Solution:
    def isAnagram(self, s, t):
        """
        Check whether t is an anagram of s.

        Args:
            s: str - input string
            t: str - input string

        Returns:
            bool - True if t is an anagram of s

        Time Complexity: O(?)
        Space Complexity: O(?)
        """
        # TODO: Implement solution
        pass


# Example usage (for testing locally)
if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    result = solution.isAnagram("anagram", "nagaram")
    print(f"Test 1: {result}")

    # Test case 2
    result = solution.isAnagram("rat", "car")
    print(f"Test 2: {result}")
