"""
LeetCode 658: Find K Closest Elements

Given a sorted integer array arr, two integers k and x, return the k closest integers to
x in the array. The result should also be sorted in ascending order.

An integer a is closer to x than an integer b if:

- |a - x| < |b - x|, or
- |a - x| == |b - x| and a < b

Example 1:
Input: arr = [1,2,3,4,5], k = 4, x = 3
Output: [1,2,3,4]

Example 2:
Input: arr = [1,1,2,3,4,5], k = 4, x = -1
Output: [1,1,2,3]

Constraints:
- 1 <= k <= arr.length
- 1 <= arr.length <= 10^4
- arr is sorted in ascending order.
- -10^4 <= arr[i], x <= 10^4
"""


class Solution:
    def findClosestElements(self, arr, k, x):
        """
        Find the k closest integers to x in a sorted array.

        Args:
            arr: List[int] - sorted array
            k: int - number of elements to return
            x: int - target value

        Returns:
            List[int] - the k closest integers in ascending order

        Time Complexity: O(?)
        Space Complexity: O(?)
        """
        # TODO: Implement solution
        pass


# Example usage (for testing locally)
if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    result = solution.findClosestElements([1, 2, 3, 4, 5], 4, 3)
    print(f"Test 1: {result}")

    # Test case 2
    result = solution.findClosestElements([1, 1, 2, 3, 4, 5], 4, -1)
    print(f"Test 2: {result}")
