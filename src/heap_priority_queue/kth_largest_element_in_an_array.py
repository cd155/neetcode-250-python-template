"""
LeetCode 215: Kth Largest Element in an Array

Given an integer array nums and an integer k, return the kth largest element in the
array.

Note that it is the kth largest element in the sorted order, not the kth distinct
element.

Can you solve it without sorting?

Example 1:
Input: nums = [3,2,1,5,6,4], k = 2
Output: 5

Example 2:
Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4

Constraints:
- 1 <= k <= nums.length <= 10^5
- -10^4 <= nums[i] <= 10^4
"""


class Solution:
    def findKthLargest(self, nums, k):
        """
        Find the k-th largest element without sorting.

        Args:
            nums: List[int] - array of integers
            k: int - rank (1-indexed)

        Returns:
            int - k-th largest element

        Time Complexity: O(?)
        Space Complexity: O(?)
        """
        # TODO: Implement solution
        pass


# Example usage (for testing locally)
if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    result = solution.findKthLargest([3, 2, 1, 5, 6, 4], 2)
    print(f"Test 1: {result}")

    # Test case 2
    result = solution.findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4)
    print(f"Test 2: {result}")
