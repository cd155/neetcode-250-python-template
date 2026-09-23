"""
LeetCode 77: Combinations

Given two integers n and k, return all possible combinations of k numbers chosen from
the range [1, n].

You may return the answer in any order.

Example 1:
Input: n = 4, k = 2
Output: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
Explanation:
There are 4 choose 2 = 6 total combinations.
Note that combinations are unordered, i.e., [1,2] and [2,1] are considered to be the
same combination.

Example 2:
Input: n = 1, k = 1
Output: [[1]]
Explanation: There is 1 choose 1 = 1 total combination.

Constraints:
- 1 <= n <= 20
- 1 <= k <= n
"""


class Solution:
    def combine(self, n, k):
        """
        Return all combinations of k numbers chosen from 1 to n.

        Args:
            n: int - numbers are chosen from 1 to n
            k: int - size of each combination

        Returns:
            List[List[int]] - all combinations in any order

        Time Complexity: O(?)
        Space Complexity: O(?)
        """
        # TODO: Implement solution
        pass


# Example usage (for testing locally)
if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    result = solution.combine(4, 2)
    print(f"Test 1: {result}")

    # Test case 2
    result = solution.combine(1, 1)
    print(f"Test 2: {result}")
