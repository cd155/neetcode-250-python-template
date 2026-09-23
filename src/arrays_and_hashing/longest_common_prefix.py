"""
LeetCode 14: Longest Common Prefix

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:
Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:
Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

Constraints:
- 1 <= strs.length <= 200
- 0 <= strs[i].length <= 200
- strs[i] consists of only lowercase English letters if it is non-empty.
"""


class Solution:
    def longestCommonPrefix(self, strs):
        """
        Find the longest common prefix among an array of strings.

        Args:
            strs: List[str] - list of strings

        Returns:
            str - longest common prefix, or an empty string

        Time Complexity: O(?)
        Space Complexity: O(?)
        """
        # TODO: Implement solution
        pass


# Example usage (for testing locally)
if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    result = solution.longestCommonPrefix(["flower", "flow", "flight"])
    print(f"Test 1: {result!r}")

    # Test case 2
    result = solution.longestCommonPrefix(["dog", "racecar", "car"])
    print(f"Test 2: {result!r}")
