"""
LeetCode 46: Permutations

Given an array nums of distinct integers, return all the possible permutations. You can
return the answer in any order.

Example 1:
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

Example 2:
Input: nums = [0,1]
Output: [[0,1],[1,0]]

Example 3:
Input: nums = [1]
Output: [[1]]

Constraints:
- 1 <= nums.length <= 6
- -10 <= nums[i] <= 10
- All the integers of nums are unique.
"""


class Solution:
    def permute(self, nums):
        """
        Return all permutations of distinct integers.

        Args:
            nums: List[int] - array of distinct integers

        Returns:
            List[List[int]] - all permutations in any order

        Time Complexity: O(?)
        Space Complexity: O(?)
        """
        # TODO: Implement solution
        pass


# Example usage (for testing locally)
if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    result = solution.permute([1, 2, 3])
    print(f"Test 1: {result}")

    # Test case 2
    result = solution.permute([0, 1])
    print(f"Test 2: {result}")
