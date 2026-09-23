"""
LeetCode 3: Longest Substring Without Repeating Characters

Given a string s, find the length of the longest substring without duplicate characters.

Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation:
The answer is "abc", with the length of 3. Note that "bca" and "cab" are also correct
answers.

Example 2:
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
Input: s = "pwwkew"
Output: 3
Explanation:
The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

Constraints:
- 0 <= s.length <= 10^5
- s consists of English letters, digits, symbols and spaces.
"""


class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        Length of the longest substring without repeating characters.

        Args:
            s: str - input string

        Returns:
            int - length of the longest such substring

        Time Complexity: O(?)
        Space Complexity: O(?)
        """
        # TODO: Implement solution
        pass


# Example usage (for testing locally)
if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    result = solution.lengthOfLongestSubstring("abcabcbb")
    print(f"Test 1: {result}")

    # Test case 2
    result = solution.lengthOfLongestSubstring("bbbbb")
    print(f"Test 2: {result}")
