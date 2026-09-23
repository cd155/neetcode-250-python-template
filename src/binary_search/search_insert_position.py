"""
LeetCode 35: Search Insert Position

Given a sorted array of distinct integers and a target value, return the index if the
target is found. If not, return the index where it would be if it were inserted in
order.

You must write an algorithm with O(log n) runtime complexity.

Example 1:
Input: nums = [1,3,5,6], target = 5
Output: 2

Example 2:
Input: nums = [1,3,5,6], target = 2
Output: 1

Example 3:
Input: nums = [1,3,5,6], target = 7
Output: 4

Constraints:
- 1 <= nums.length <= 10^4
- -10^4 <= nums[i] <= 10^4
- nums contains distinct values sorted in ascending order.
- -10^4 <= target <= 10^4
"""


class Solution:
    def searchInsert(self, nums, target):
        """
        Find the index of target, or where it would be inserted, in O(log n).

        Args:
            nums: List[int] - sorted array of distinct integers
            target: int - target value

        Returns:
            int - index of target or its insert position

        Time Complexity: O(?)
        Space Complexity: O(?)
        """
        # TODO: Implement solution
        pass


# Example usage (for testing locally)
if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    result = solution.searchInsert([1, 3, 5, 6], 5)
    print(f"Test 1: {result}")

    # Test case 2
    result = solution.searchInsert([1, 3, 5, 6], 2)
    print(f"Test 2: {result}")
