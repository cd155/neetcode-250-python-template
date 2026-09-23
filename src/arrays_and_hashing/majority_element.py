"""
LeetCode 169: Majority Element

Given an array nums of size n, return the majority element.

The majority element is the element that appears more than floor(n / 2) times. You may
assume that the majority element always exists in the array.

Example 1:
Input: nums = [3,2,3]
Output: 3

Example 2:
Input: nums = [2,2,1,1,1,2,2]
Output: 2

Constraints:
- n == nums.length
- 1 <= n <= 5 * 10^4
- -10^9 <= nums[i] <= 10^9
- The input is generated such that a majority element will exist in the array.

Follow-up: Could you solve the problem in linear time and in O(1) space?
"""


class Solution:
    def majorityElement(self, nums):
        """
        Find the element that appears more than n / 2 times.

        Args:
            nums: List[int] - array of integers

        Returns:
            int - the majority element

        Time Complexity: O(?)
        Space Complexity: O(?)
        """
        # TODO: Implement solution
        pass


# Example usage (for testing locally)
if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    result = solution.majorityElement([3, 2, 3])
    print(f"Test 1: {result}")

    # Test case 2
    result = solution.majorityElement([2, 2, 1, 1, 1, 2, 2])
    print(f"Test 2: {result}")
