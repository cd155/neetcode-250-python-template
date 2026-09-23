"""
LeetCode 287: Find the Duplicate Number

Given an array of integers nums containing n + 1 integers where each integer is in the
range [1, n] inclusive.

There is only one repeated number in nums, return this repeated number.

You must solve the problem without modifying the array nums and using only constant
extra space.

Example 1:
Input: nums = [1,3,4,2,2]
Output: 2

Example 2:
Input: nums = [3,1,3,4,2]
Output: 3

Example 3:
Input: nums = [3,3,3,3,3]
Output: 3

Constraints:
- 1 <= n <= 10^5
- nums.length == n + 1
- 1 <= nums[i] <= n
- All the integers in nums appear only once except for precisely one integer which
  appears two or more times.
- How can we prove that at least one duplicate number must exist in nums?
- Can you solve the problem in linear runtime complexity?

Follow up:
"""


class Solution:
    def findDuplicate(self, nums):
        """
        Find the repeated number without modifying nums, using O(1) extra space.

        Args:
            nums: List[int] - n + 1 integers in the range [1, n]

        Returns:
            int - the repeated number

        Time Complexity: O(?)
        Space Complexity: O(?)
        """
        # TODO: Implement solution
        pass


# Example usage (for testing locally)
if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    result = solution.findDuplicate([1, 3, 4, 2, 2])
    print(f"Test 1: {result}")

    # Test case 2
    result = solution.findDuplicate([3, 1, 3, 4, 2])
    print(f"Test 2: {result}")
