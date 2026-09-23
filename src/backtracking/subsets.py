"""
LeetCode 78: Subsets

Given an integer array nums of unique elements, return all possible subsets (the power
set).

The solution set must not contain duplicate subsets. Return the solution in any order.

Example 1:
Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

Example 2:
Input: nums = [0]
Output: [[],[0]]

Constraints:
- 1 <= nums.length <= 10
- -10 <= nums[i] <= 10
- All the numbers of nums are unique.
"""


class Solution:
    def subsets(self, nums):
        """
        Return all possible subsets (the power set).

        Args:
            nums: List[int] - array of unique integers

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
    result = solution.subsets([1, 2, 3])
    print(f"Test 1: {result}")

    # Test case 2
    result = solution.subsets([0])
    print(f"Test 2: {result}")
