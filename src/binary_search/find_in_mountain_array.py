"""
LeetCode 1095: Find in Mountain Array

(This problem is an interactive problem.)

You may recall that an array arr is a mountain array if and only if:

- arr.length >= 3
- There exists some i with 0 < i < arr.length - 1 such that:
  - arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
  - arr[i] > arr[i + 1] > ... > arr[arr.length - 1]

Given a mountain array mountainArr, return the minimum index such that
mountainArr.get(index) == target. If such an index does not exist, return -1.

You cannot access the mountain array directly. You may only access the array using a
MountainArray interface:

- MountainArray.get(k) returns the element of the array at index k (0-indexed).
- MountainArray.length() returns the length of the array.

Submissions making more than 100 calls to MountainArray.get will be judged Wrong Answer.
Also, any solutions that attempt to circumvent the judge will result in
disqualification.

Example 1:
Input: mountainArr = [1,2,3,4,5,3,1], target = 3
Output: 2
Explanation:
3 exists in the array, at index=2 and index=5. Return the minimum index, which is 2.

Example 2:
Input: mountainArr = [0,1,2,4,2,1], target = 3
Output: -1
Explanation: 3 does not exist in the array, so we return -1.

Constraints:
- 3 <= mountainArr.length() <= 10^4
- 0 <= target <= 10^9
- 0 <= mountainArr.get(index) <= 10^9
"""


class MountainArray:
    """
    The MountainArray interface is predefined on LeetCode. This local version wraps a list.
    You may only call get(index) and length().
    """

    def __init__(self, arr):
        self._arr = arr

    def get(self, index):
        return self._arr[index]

    def length(self):
        return len(self._arr)


class Solution:
    def findInMountainArray(self, target, mountain_arr):
        """
        Find the minimum index of target in a mountain array using at most 100 calls.

        Args:
            target: int - value to find
            mountain_arr: MountainArray - mountain array interface (get, length)

        Returns:
            int - minimum index of target, or -1

        Time Complexity: O(?)
        Space Complexity: O(?)
        """
        # TODO: Implement solution
        pass


# Example usage (for testing locally)
if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    result = solution.findInMountainArray(3, MountainArray([1, 2, 3, 4, 5, 3, 1]))
    print(f"Test 1: {result}")

    # Test case 2
    result = solution.findInMountainArray(3, MountainArray([0, 1, 2, 4, 2, 1]))
    print(f"Test 2: {result}")
