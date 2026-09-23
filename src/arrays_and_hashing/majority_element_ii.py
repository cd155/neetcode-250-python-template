"""
LeetCode 229: Majority Element II

Given an integer array of size n, find all elements that appear more than floor(n / 3)
times.

Example 1:
Input: nums = [3,2,3]
Output: [3]

Example 2:
Input: nums = [1]
Output: [1]

Example 3:
Input: nums = [1,2]
Output: [1,2]

Constraints:
- 1 <= nums.length <= 5 * 10^4
- -10^9 <= nums[i] <= 10^9

Follow up: Could you solve the problem in linear time and in O(1) space?
"""


class Solution:
    def majorityElement(self, nums):
        """
        Find all elements that appear more than n / 3 times.

        Args:
            nums: List[int] - array of integers

        Returns:
            List[int] - those elements in any order

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
    result = solution.majorityElement([1])
    print(f"Test 2: {result}")
