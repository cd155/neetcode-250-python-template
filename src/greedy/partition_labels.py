"""
LeetCode 763: Partition Labels

You are given a string s. We want to partition the string into as many parts as possible
so that each letter appears in at most one part. For example, the string "ababcc" can be
partitioned into ["abab", "cc"], but partitions such as ["aba", "bcc"] or ["ab", "ab",
"cc"] are invalid.

Note that the partition is done so that after concatenating all the parts in order, the
resultant string should be s.

Return a list of integers representing the size of these parts.

Example 1:
Input: s = "ababcbacadefegdehijhklij"
Output: [9,7,8]
Explanation:
The partition is "ababcbaca", "defegde", "hijhklij".
This is a partition so that each letter appears in at most one part.
A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits s into
less parts.

Example 2:
Input: s = "eccbbbbdec"
Output: [10]

Constraints:
- 1 <= s.length <= 500
- s consists of lowercase English letters.
"""


class Solution:
    def partitionLabels(self, s):
        """
        Partition s so each letter appears in at most one part.

        Args:
            s: str - input string

        Returns:
            List[int] - sizes of the parts

        Time Complexity: O(?)
        Space Complexity: O(?)
        """
        # TODO: Implement solution
        pass


# Example usage (for testing locally)
if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    result = solution.partitionLabels("ababcbacadefegdehijhklij")
    print(f"Test 1: {result}")

    # Test case 2
    result = solution.partitionLabels("eccbbbbdec")
    print(f"Test 2: {result}")
