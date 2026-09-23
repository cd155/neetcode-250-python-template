"""
LeetCode 136: Single Number

Given a non-empty array of integers nums, every element appears twice except for one.
Find that single one.

You must implement a solution with a linear runtime complexity and use only constant
extra space.

Example 1:
Input: nums = [2,2,1]
Output: 1

Example 2:
Input: nums = [4,1,2,1,2]
Output: 4

Example 3:
Input: nums = [1]
Output: 1

Constraints:
- 1 <= nums.length <= 3 * 10^4
- -3 * 10^4 <= nums[i] <= 3 * 10^4
- Each element in the array appears twice except for one element which appears only
  once.
"""


class Solution:
    def singleNumber(self, nums):
        """
        Find the element that appears only once (the rest appear twice).

        Args:
            nums: List[int] - array of integers

        Returns:
            int - the single element

        Time Complexity: O(?)
        Space Complexity: O(?)
        """
        # TODO: Implement solution
        pass


# Example usage (for testing locally)
if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    result = solution.singleNumber([2, 2, 1])
    print(f"Test 1: {result}")

    # Test case 2
    result = solution.singleNumber([4, 1, 2, 1, 2])
    print(f"Test 2: {result}")
