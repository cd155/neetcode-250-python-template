"""
LeetCode 1: Two Sum

You are given an array of integers nums and an integer target, return indices of the two
numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the
same element twice.

You can return the answer in any order.

Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:
Input: nums = [3,3], target = 6
Output: [0,1]

Constraints:
- 2 <= nums.length <= 10^4
- -10^9 <= nums[i] <= 10^9
- -10^9 <= target <= 10^9
- Only one valid answer exists.

Follow-up: Can you come up with an algorithm that is less than O(n^2) time complexity?
"""


class Solution:
    def twoSum(self, nums, target):
        """
        Find the indices of the two numbers that add up to target.

        Args:
            nums: List[int] - array of integers
            target: int - target sum

        Returns:
            List[int] - indices of the two numbers

        Time Complexity: O(?)
        Space Complexity: O(?)
        """
        # TODO: Implement solution
        pass


# Example usage (for testing locally)
if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    result = solution.twoSum([2, 7, 11, 15], 9)
    print(f"Test 1: {result}")

    # Test case 2
    result = solution.twoSum([3, 2, 4], 6)
    print(f"Test 2: {result}")
