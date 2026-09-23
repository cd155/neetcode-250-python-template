"""
LeetCode 239: Sliding Window Maximum

You are given an array of integers nums, there is a sliding window of size k which is
moving from the very left of the array to the very right. You can only see the k numbers
in the window. Each time the sliding window moves right by one position.

Return the max sliding window.

Example 1:
Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]
Explanation:
Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7

Example 2:
Input: nums = [1], k = 1
Output: [1]

Constraints:
- 1 <= nums.length <= 10^5
- -10^4 <= nums[i] <= 10^4
- 1 <= k <= nums.length
"""


class Solution:
    def maxSlidingWindow(self, nums, k):
        """
        Maximum of each sliding window of size k.

        Args:
            nums: List[int] - array of integers
            k: int - window size

        Returns:
            List[int] - maximum of each window

        Time Complexity: O(?)
        Space Complexity: O(?)
        """
        # TODO: Implement solution
        pass


# Example usage (for testing locally)
if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    result = solution.maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3)
    print(f"Test 1: {result}")

    # Test case 2
    result = solution.maxSlidingWindow([1], 1)
    print(f"Test 2: {result}")
