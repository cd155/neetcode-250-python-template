"""
LeetCode 47: Permutations II

Given a collection of numbers, nums, that might contain duplicates, return all possible
unique permutations in any order.

Example 1:
Input: nums = [1,1,2]
Output: [[1,1,2],
        [1,2,1],
        [2,1,1]]

Example 2:
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

Constraints:
- 1 <= nums.length <= 8
- -10 <= nums[i] <= 10
"""


class Solution:
    def permuteUnique(self, nums):
        """
        Return all unique permutations of numbers that may contain duplicates.

        Args:
            nums: List[int] - array that may contain duplicates

        Returns:
            List[List[int]] - unique permutations in any order

        Time Complexity: O(?)
        Space Complexity: O(?)
        """
        # TODO: Implement solution
        pass


# Example usage (for testing locally)
if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    result = solution.permuteUnique([1, 1, 2])
    print(f"Test 1: {result}")

    # Test case 2
    result = solution.permuteUnique([1, 2, 3])
    print(f"Test 2: {result}")
