"""
LeetCode 18: 4Sum

Given an array nums of n integers, return an array of all the unique quadruplets
[nums[a], nums[b], nums[c], nums[d]] such that:

- 0 <= a, b, c, d < n
- a, b, c, and d are distinct.
- nums[a] + nums[b] + nums[c] + nums[d] == target

You may return the answer in any order.

Example 1:
Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]

Example 2:
Input: nums = [2,2,2,2,2], target = 8
Output: [[2,2,2,2]]

Constraints:
- 1 <= nums.length <= 200
- -10^9 <= nums[i] <= 10^9
- -10^9 <= target <= 10^9
"""


class Solution:
    def fourSum(self, nums, target):
        """
        Find all unique quadruplets that sum to target.

        Args:
            nums: List[int] - array of integers
            target: int - target sum

        Returns:
            List[List[int]] - unique quadruplets in any order

        Time Complexity: O(?)
        Space Complexity: O(?)
        """
        # TODO: Implement solution
        pass


# Example usage (for testing locally)
if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    result = solution.fourSum([1, 0, -1, 0, -2, 2], 0)
    print(f"Test 1: {result}")

    # Test case 2
    result = solution.fourSum([2, 2, 2, 2, 2], 8)
    print(f"Test 2: {result}")
