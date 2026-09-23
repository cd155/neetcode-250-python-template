"""
LeetCode 49: Group Anagrams

Given an array of strings strs, group the anagrams together. You can return the answer
in any order.

Example 1:
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Explanation:
- There is no string in strs that can be rearranged to form "bat".
- The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
- The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form
each other.

Example 2:
Input: strs = [""]
Output: [[""]]

Example 3:
Input: strs = ["a"]
Output: [["a"]]

Constraints:
- 1 <= strs.length <= 10^4
- 0 <= strs[i].length <= 100
- strs[i] consists of lowercase English letters.
"""


class Solution:
    def groupAnagrams(self, strs):
        """
        Group the strings that are anagrams of each other.

        Args:
            strs: List[str] - list of strings

        Returns:
            List[List[str]] - groups of anagrams in any order

        Time Complexity: O(?)
        Space Complexity: O(?)
        """
        # TODO: Implement solution
        pass


# Example usage (for testing locally)
if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    result = solution.groupAnagrams(strs)
    print(f"Test 1: {result}")

    # Test case 2
    result = solution.groupAnagrams([""])
    print(f"Test 2: {result}")
