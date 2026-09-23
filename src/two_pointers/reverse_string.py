"""
LeetCode 344: Reverse String

Write a function that reverses a string. The input string is given as an array of
characters s.

You must do this by modifying the input array in-place with O(1) extra memory.

Example 1:
Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]

Example 2:
Input: s = ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]

Constraints:
- 1 <= s.length <= 10^5
- s[i] is a printable ascii character.
"""


class Solution:
    def reverseString(self, s):
        """
        Reverse the array of characters in-place.

        Args:
            s: List[str] - array of characters

        Returns:
            None - s is modified in-place

        Time Complexity: O(?)
        Space Complexity: O(?)
        """
        # TODO: Implement solution
        pass


# Example usage (for testing locally)
if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    s = ["h", "e", "l", "l", "o"]
    solution.reverseString(s)
    print(f"Test 1: {s}")

    # Test case 2
    s = ["H", "a", "n", "n", "a", "h"]
    solution.reverseString(s)
    print(f"Test 2: {s}")
