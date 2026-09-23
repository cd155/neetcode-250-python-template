"""
LeetCode 140: Word Break II

Given a string s and a dictionary of strings wordDict, add spaces in s to construct a
sentence where each word is a valid dictionary word. Return all such possible sentences
in any order.

Note that the same word in the dictionary may be reused multiple times in the
segmentation.

Example 1:
Input: s = "catsanddog", wordDict = ["cat","cats","and","sand","dog"]
Output: ["cats and dog","cat sand dog"]

Example 2:
Input: s = "pineapplepenapple", wordDict = ["apple","pen","applepen","pine","pineapple"]
Output: ["pine apple pen apple","pineapple pen apple","pine applepen apple"]
Explanation: Note that you are allowed to reuse a dictionary word.

Example 3:
Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: []

Constraints:
- 1 <= s.length <= 20
- 1 <= wordDict.length <= 1000
- 1 <= wordDict[i].length <= 10
- s and wordDict[i] consist of only lowercase English letters.
- All the strings of wordDict are unique.
- Input is generated in a way that the length of the answer doesn't exceed 10^5.
"""


class Solution:
    def wordBreak(self, s, wordDict):
        """
        Add spaces to s to build every sentence made of dictionary words.

        Args:
            s: str - input string
            wordDict: List[str] - dictionary of words

        Returns:
            List[str] - all sentences in any order

        Time Complexity: O(?)
        Space Complexity: O(?)
        """
        # TODO: Implement solution
        pass


# Example usage (for testing locally)
if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    result = solution.wordBreak("catsanddog", ["cat", "cats", "and", "sand", "dog"])
    print(f"Test 1: {result}")

    # Test case 2
    wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
    result = solution.wordBreak("pineapplepenapple", wordDict)
    print(f"Test 2: {result}")
