"""
LeetCode 17: Letter Combinations of a Phone Number

Given a string containing digits from 2-9 inclusive, return all possible letter
combinations that the number could represent. Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) is given below. Note
that 1 does not map to any letters.

Example 1:
Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

Example 2:
Input: digits = "2"
Output: ["a","b","c"]

Constraints:
- 1 <= digits.length <= 4
- digits[i] is a digit in the range ['2', '9'].
"""


class Solution:
    def letterCombinations(self, digits):
        """
        Letter combinations a phone number's digits could represent.

        Args:
            digits: str - digits from 2 to 9

        Returns:
            List[str] - all combinations in any order

        Time Complexity: O(?)
        Space Complexity: O(?)
        """
        # TODO: Implement solution
        pass


# Example usage (for testing locally)
if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    result = solution.letterCombinations("23")
    print(f"Test 1: {result}")

    # Test case 2
    result = solution.letterCombinations("2")
    print(f"Test 2: {result}")
