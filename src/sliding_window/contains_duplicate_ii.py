"""
LeetCode 219: Contains Duplicate II

Given an integer array nums and an integer k, return true if there are two distinct
indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.

Example 1:
Input: nums = [1,2,3,1], k = 3
Output: true

Example 2:
Input: nums = [1,0,1,1], k = 1
Output: true

Example 3:
Input: nums = [1,2,3,1,2,3], k = 2
Output: false

Constraints:
- 1 <= nums.length <= 10^5
- -10^9 <= nums[i] <= 10^9
- 0 <= k <= 10^5
"""


class Solution:
    def containsNearbyDuplicate(self, nums, k):
        """
        Check whether two equal values have indices at most k apart.

        Args:
            nums: List[int] - array of integers
            k: int - maximum index distance

        Returns:
            bool - True if such a pair exists

        Time Complexity: O(?)
        Space Complexity: O(?)
        """
        # TODO: Implement solution
        pass


# Example usage (for testing locally)
if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    result = solution.containsNearbyDuplicate([1, 2, 3, 1], 3)
    print(f"Test 1: {result}")

    # Test case 2
    result = solution.containsNearbyDuplicate([1, 0, 1, 1], 1)
    print(f"Test 2: {result}")
