"""
LeetCode 252: Meeting Rooms

You are given an array of meeting times intervals where intervals[i] = [starti, endi].

A person can attend all meetings if no two meeting intervals overlap. Meetings ending at
time t and starting at time t do not overlap.

Return true if a person can attend all meetings. Otherwise, return false.

Example 1:
Input: intervals = [[0,30],[5,10],[15,20]]
Output: false

Example 2:
Input: intervals = [[7,10],[2,4]]
Output: true

Constraints:
- 0 <= intervals.length <= 10^4
- intervals[i].length == 2
- 0 <= starti < endi <= 10^6
"""


class Solution:
    def canAttendMeetings(self, intervals):
        """
        Check whether a person could attend all meetings.

        Args:
            intervals: List[List[int]] - meeting time intervals [start, end]

        Returns:
            bool - True if no meetings overlap

        Time Complexity: O(?)
        Space Complexity: O(?)
        """
        # TODO: Implement solution
        pass


# Example usage (for testing locally)
if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    result = solution.canAttendMeetings([[0, 30], [5, 10], [15, 20]])
    print(f"Test 1: {result}")

    # Test case 2
    result = solution.canAttendMeetings([[7, 10], [2, 4]])
    print(f"Test 2: {result}")
