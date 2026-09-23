"""
LeetCode 217: Contains Duplicate

Given an integer array nums, return true if any value appears at least twice in the
array, and return false if every element is distinct.

Example 1:
Input: nums = [1,2,3,1]
Output: true
Explanation: The element 1 occurs at the indices 0 and 3.

Example 2:
Input: nums = [1,2,3,4]
Output: false
Explanation: All elements are distinct.

Example 3:
Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true

Constraints:
- 1 <= nums.length <= 10^5
- -10^9 <= nums[i] <= 10^9
"""


class Solution:
    def containsDuplicate(self, nums):
        """
        Check whether any value appears at least twice.

        Args:
            nums: List[int] - array of integers

        Returns:
            bool - True if there is a duplicate

        Time Complexity: O(?)
        Space Complexity: O(?)
        """
        # TODO: Implement solution
        pass


# Example usage (for testing locally)
if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    result = solution.containsDuplicate([1, 2, 3, 1])
    print(f"Test 1: {result}")

    # Test case 2
    result = solution.containsDuplicate([1, 2, 3, 4])
    print(f"Test 2: {result}")
