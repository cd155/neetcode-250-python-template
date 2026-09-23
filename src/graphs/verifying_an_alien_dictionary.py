"""
LeetCode 953: Verifying an Alien Dictionary

In an alien language, surprisingly, they also use English lowercase letters, but
possibly in a different order. The order of the alphabet is some permutation of
lowercase letters.

Given a sequence of words written in the alien language, and the order of the alphabet,
return true if and only if the given words are sorted lexicographically in this alien
language.

Example 1:
Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
Output: true
Explanation: As 'h' comes before 'l' in this language, then the sequence is sorted.

Example 2:
Input: words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
Output: false
Explanation:
As 'd' comes after 'l' in this language, then words[0] > words[1], hence the sequence is
unsorted.

Example 3:
Input: words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"
Output: false
Explanation:
The first three characters "app" match, and the second string is shorter (in size.)
According to lexicographical rules "apple" > "app", because 'l' > '{}', where '{}' is
defined as the blank character which is less than any other character (More info).

Constraints:
- 1 <= words.length <= 100
- 1 <= words[i].length <= 20
- order.length == 26
- All characters in words[i] and order are English lowercase letters.
"""


class Solution:
    def isAlienSorted(self, words, order):
        """
        Check whether words are sorted in the alien language.

        Args:
            words: List[str] - list of words
            order: str - order of the alien alphabet

        Returns:
            bool - True if words are sorted lexicographically

        Time Complexity: O(?)
        Space Complexity: O(?)
        """
        # TODO: Implement solution
        pass


# Example usage (for testing locally)
if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    result = solution.isAlienSorted(["hello", "leetcode"], "hlabcdefgijkmnopqrstuvwxyz")
    print(f"Test 1: {result}")

    # Test case 2
    result = solution.isAlienSorted(["word", "world", "row"], "worldabcefghijkmnpqstuvxyz")
    print(f"Test 2: {result}")
