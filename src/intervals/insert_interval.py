"""
LeetCode 57: Insert Interval

You are given an array of non-overlapping intervals intervals where intervals[i] =
[starti, endi] represent the start and the end of the ith interval and intervals is
sorted in ascending order by starti. You are also given an interval newInterval =
[start, end] that represents the start and end of another interval.

Two intervals are considered overlapping if they share at least one point.

Insert newInterval into intervals such that intervals is still sorted in ascending order
by starti and intervals still does not have any overlapping intervals (merge overlapping
intervals if necessary).

Return intervals after the insertion.

Note that you don't need to modify intervals in-place. You can make a new array and
return it.

Example 1:
Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]

Example 2:
Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].

Constraints:
- 0 <= intervals.length <= 10^4
- intervals[i].length == 2
- 0 <= starti <= endi <= 10^5
- intervals is sorted by starti in ascending order.
- newInterval.length == 2
- 0 <= start <= end <= 10^5
"""


class Solution:
    def insert(self, intervals, newInterval):
        """
        Insert newInterval into sorted non-overlapping intervals, merging if needed.

        Args:
            intervals: List[List[int]] - non-overlapping intervals sorted by start
            newInterval: List[int] - [start, end] interval to insert

        Returns:
            List[List[int]] - intervals after the insertion

        Time Complexity: O(?)
        Space Complexity: O(?)
        """
        # TODO: Implement solution
        pass


# Example usage (for testing locally)
if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    result = solution.insert([[1, 3], [6, 9]], [2, 5])
    print(f"Test 1: {result}")

    # Test case 2
    intervals = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]
    result = solution.insert(intervals, [4, 8])
    print(f"Test 2: {result}")
