"""
LeetCode 41: First Missing Positive

Given an unsorted integer array nums. Return the smallest positive integer that is not
present in nums.

You must implement an algorithm that runs in O(n) time and uses O(1) auxiliary space.

Example 1:
Input: nums = [1,2,0]
Output: 3
Explanation: The numbers in the range [1,2] are all in the array.

Example 2:
Input: nums = [3,4,-1,1]
Output: 2
Explanation: 1 is in the array but 2 is missing.

Example 3:
Input: nums = [7,8,9,11,12]
Output: 1
Explanation: The smallest positive integer 1 is missing.

Constraints:
- 1 <= nums.length <= 10^5
- -2^31 <= nums[i] <= 2^31 - 1
"""


class Solution:
    def firstMissingPositive(self, nums):
        """
        Find the smallest missing positive integer in O(n) time and O(1) space.

        Args:
            nums: List[int] - array of integers

        Returns:
            int - smallest missing positive integer

        Time Complexity: O(?)
        Space Complexity: O(?)
        """
        # TODO: Implement solution
        pass


# Example usage (for testing locally)
if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    result = solution.firstMissingPositive([1, 2, 0])
    print(f"Test 1: {result}")

    # Test case 2
    result = solution.firstMissingPositive([3, 4, -1, 1])
    print(f"Test 2: {result}")
