"""
LeetCode 698: Partition to K Equal Sum Subsets

Given an integer array nums and an integer k, return true if it is possible to divide
this array into k non-empty subsets whose sums are all equal.

Example 1:
Input: nums = [4,3,2,3,5,2,1], k = 4
Output: true
Explanation:
It is possible to divide it into 4 subsets (5), (1, 4), (2,3), (2,3) with equal sums.

Example 2:
Input: nums = [1,2,3,4], k = 3
Output: false

Constraints:
- 1 <= k <= nums.length <= 16
- 1 <= nums[i] <= 10^4
- The frequency of each element is in the range [1, 4].
"""


class Solution:
    def canPartitionKSubsets(self, nums, k):
        """
        Check whether nums can be divided into k subsets with equal sums.

        Args:
            nums: List[int] - array of integers
            k: int - number of subsets

        Returns:
            bool - True if such a division exists

        Time Complexity: O(?)
        Space Complexity: O(?)
        """
        # TODO: Implement solution
        pass


# Example usage (for testing locally)
if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    result = solution.canPartitionKSubsets([4, 3, 2, 3, 5, 2, 1], 4)
    print(f"Test 1: {result}")

    # Test case 2
    result = solution.canPartitionKSubsets([1, 2, 3, 4], 3)
    print(f"Test 2: {result}")
