"""
LeetCode 704: Binary Search

Given an array of integers nums which is sorted in ascending order, and an integer
target, write a function to search target in nums. If target exists, then return its
index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.

Example 1:
Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4

Example 2:
Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1

Constraints:
- 1 <= nums.length <= 10^4
- -10^4 < nums[i], target < 10^4
- All the integers in nums are unique.
- nums is sorted in ascending order.
"""


class Solution:
    def search(self, nums, target):
        """
        Search for target in a sorted array in O(log n).

        Args:
            nums: List[int] - array sorted in ascending order
            target: int - target value

        Returns:
            int - index of target, or -1

        Time Complexity: O(?)
        Space Complexity: O(?)
        """
        # TODO: Implement solution
        pass


# Example usage (for testing locally)
if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    result = solution.search([-1, 0, 3, 5, 9, 12], 9)
    print(f"Test 1: {result}")

    # Test case 2
    result = solution.search([-1, 0, 3, 5, 9, 12], 2)
    print(f"Test 2: {result}")
