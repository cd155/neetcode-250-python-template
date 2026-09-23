"""
LeetCode 84: Largest Rectangle in Histogram

Given an array of integers heights representing the histogram's bar height where the
width of each bar is 1, return the area of the largest rectangle in the histogram.

Example 1:
Input: heights = [2,1,5,6,2,3]
Output: 10
Explanation:
The above is a histogram where width of each bar is 1.
The largest rectangle is shown in the red area, which has an area = 10 units.

Example 2:
Input: heights = [2,4]
Output: 4

Constraints:
- 1 <= heights.length <= 10^5
- 0 <= heights[i] <= 10^4
"""


class Solution:
    def largestRectangleArea(self, heights):
        """
        Area of the largest rectangle in the histogram.

        Args:
            heights: List[int] - bar heights, each bar has width 1

        Returns:
            int - largest rectangle area

        Time Complexity: O(?)
        Space Complexity: O(?)
        """
        # TODO: Implement solution
        pass


# Example usage (for testing locally)
if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    result = solution.largestRectangleArea([2, 1, 5, 6, 2, 3])
    print(f"Test 1: {result}")

    # Test case 2
    result = solution.largestRectangleArea([2, 4])
    print(f"Test 2: {result}")
