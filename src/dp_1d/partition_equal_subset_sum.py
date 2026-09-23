"""
LeetCode 416: Partition Equal Subset Sum

Given an integer array nums, return true if you can partition the array into two subsets
such that the sum of the elements in both subsets is equal or false otherwise.

Example 1:
Input: nums = [1,5,11,5]
Output: true
Explanation: The array can be partitioned as [1, 5, 5] and [11].

Example 2:
Input: nums = [1,2,3,5]
Output: false
Explanation: The array cannot be partitioned into equal sum subsets.

Constraints:
- 1 <= nums.length <= 200
- 1 <= nums[i] <= 100
"""


class Solution:
    def canPartition(self, nums):
        """
        Check whether nums can be split into two subsets with equal sums.

        Args:
            nums: List[int] - array of integers

        Returns:
            bool - True if such a partition exists

        Time Complexity: O(?)
        Space Complexity: O(?)
        """
        # TODO: Implement solution
        pass


# Example usage (for testing locally)
if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    result = solution.canPartition([1, 5, 11, 5])
    print(f"Test 1: {result}")

    # Test case 2
    result = solution.canPartition([1, 2, 3, 5])
    print(f"Test 2: {result}")
