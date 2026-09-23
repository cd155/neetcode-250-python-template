"""
LeetCode 90: Subsets II

Given an integer array nums that may contain duplicates, return all possible subsets
(the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

Example 1:
Input: nums = [1,2,2]
Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]

Example 2:
Input: nums = [0]
Output: [[],[0]]

Constraints:
- 1 <= nums.length <= 10
- -10 <= nums[i] <= 10
"""


class Solution:
    def subsetsWithDup(self, nums):
        """
        Return all subsets without duplicate subsets.

        Args:
            nums: List[int] - array that may contain duplicates

        Returns:
            List[List[int]] - all subsets in any order

        Time Complexity: O(?)
        Space Complexity: O(?)
        """
        # TODO: Implement solution
        pass


# Example usage (for testing locally)
if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    result = solution.subsetsWithDup([1, 2, 2])
    print(f"Test 1: {result}")

    # Test case 2
    result = solution.subsetsWithDup([0])
    print(f"Test 2: {result}")
