"""
LeetCode 22: Generate Parentheses

Given n pairs of parentheses, write a function to generate all combinations of
well-formed parentheses.

Example 1:
Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]

Example 2:
Input: n = 1
Output: ["()"]

Constraints:
- 1 <= n <= 8
"""


class Solution:
    def generateParenthesis(self, n):
        """
        Generate all combinations of n pairs of well-formed parentheses.

        Args:
            n: int - number of pairs

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
    result = solution.generateParenthesis(3)
    print(f"Test 1: {result}")

    # Test case 2
    result = solution.generateParenthesis(1)
    print(f"Test 2: {result}")
