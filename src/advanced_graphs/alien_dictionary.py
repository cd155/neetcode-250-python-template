"""
LeetCode 269: Alien Dictionary

There is a new alien language that uses the English alphabet. However, the order of the
letters is unknown to you.

You are given a list of strings words from the alien language's dictionary. Now it is
claimed that the strings in words are sorted lexicographically by the rules of this new
language.

If this claim is incorrect, and the given arrangement of string in words cannot
correspond to any order of letters, return "".

Otherwise, return a string of the unique letters in the new alien language sorted in
lexicographically increasing order by the new language's rules. If there are multiple
solutions, return any of them.

Example 1:
Input: words = ["wrt","wrf","er","ett","rftt"]
Output: "wertf"

Example 2:
Input: words = ["z","x"]
Output: "zx"

Example 3:
Input: words = ["z","x","z"]
Output: ""
Explanation: The order is invalid, so return "".

Constraints:
- 1 <= words.length <= 100
- 1 <= words[i].length <= 100
- words[i] consists of only lowercase English letters.
"""


class Solution:
    def alienOrder(self, words):
        """
        Derive the order of letters in an alien language.

        Args:
            words: List[str] - words sorted in the alien language

        Returns:
            str - any valid order of letters, or an empty string

        Time Complexity: O(?)
        Space Complexity: O(?)
        """
        # TODO: Implement solution
        pass


# Example usage (for testing locally)
if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    result = solution.alienOrder(["wrt", "wrf", "er", "ett", "rftt"])
    print(f"Test 1: {result!r}")

    # Test case 2
    result = solution.alienOrder(["z", "x"])
    print(f"Test 2: {result!r}")
