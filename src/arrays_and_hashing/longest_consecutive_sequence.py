"""
LeetCode 128: Longest Consecutive Sequence

Given an unsorted array of integers nums, return the length of the longest consecutive
elements sequence.

You must write an algorithm that runs in O(n) time.

Example 1:
Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation:
The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

Example 2:
Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9

Example 3:
Input: nums = [1,0,1,2]
Output: 3

Constraints:
- 0 <= nums.length <= 10^5
- -10^9 <= nums[i] <= 10^9
"""


class Solution:
    def longestConsecutive(self, nums):
        """
        Find the length of the longest consecutive elements sequence in O(n).

        Args:
            nums: List[int] - array of integers

        Returns:
            int - length of the longest consecutive sequence

        Time Complexity: O(?)
        Space Complexity: O(?)
        """
        # TODO: Implement solution
        pass


# Example usage (for testing locally)
if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    result = solution.longestConsecutive([100, 4, 200, 1, 3, 2])
    print(f"Test 1: {result}")

    # Test case 2
    result = solution.longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1])
    print(f"Test 2: {result}")
