"""
LeetCode 131: Palindrome Partitioning

Given a string s, partition s such that every substring of the partition is a
palindrome. Return all possible palindrome partitioning of s.

Example 1:
Input: s = "aab"
Output: [["a","a","b"],["aa","b"]]

Example 2:
Input: s = "a"
Output: [["a"]]

Constraints:
- 1 <= s.length <= 16
- s contains only lowercase English letters.
"""


class Solution:
    def partition(self, s):
        """
        Partition s so that every substring is a palindrome.

        Args:
            s: str - input string

        Returns:
            List[List[str]] - all palindrome partitionings in any order

        Time Complexity: O(?)
        Space Complexity: O(?)
        """
        # TODO: Implement solution
        pass


# Example usage (for testing locally)
if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    result = solution.partition("aab")
    print(f"Test 1: {result}")

    # Test case 2
    result = solution.partition("a")
    print(f"Test 2: {result}")
