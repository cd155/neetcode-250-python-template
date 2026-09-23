"""
LeetCode 1462: Course Schedule IV

There are a total of numCourses courses you have to take, labeled from 0 to numCourses -
1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that
you must take course ai first if you want to take course bi.

- For example, the pair [0, 1] indicates that you have to take course 0 before you can
  take course 1.

Prerequisites can also be indirect. If course a is a prerequisite of course b, and
course b is a prerequisite of course c, then course a is a prerequisite of course c.

You are also given an array queries where queries[j] = [uj, vj]. For the jth query, you
should answer whether course uj is a prerequisite of course vj or not.

Return a boolean array answer, where answer[j] is the answer to the jth query.

Example 1:
Input: numCourses = 2, prerequisites = [[1,0]], queries = [[0,1],[1,0]]
Output: [false,true]
Explanation:
The pair [1, 0] indicates that you have to take course 1 before you can take course 0.
Course 0 is not a prerequisite of course 1, but the opposite is true.

Example 2:
Input: numCourses = 2, prerequisites = [], queries = [[1,0],[0,1]]
Output: [false,false]
Explanation: There are no prerequisites, and each course is independent.

Example 3:
Input: numCourses = 3, prerequisites = [[1,2],[1,0],[2,0]], queries = [[1,0],[1,2]]
Output: [true,true]

Constraints:
- 2 <= numCourses <= 100
- 0 <= prerequisites.length <= (numCourses * (numCourses - 1) / 2)
- prerequisites[i].length == 2
- 0 <= ai, bi <= numCourses - 1
- ai != bi
- All the pairs [ai, bi] are unique.
- The prerequisites graph has no cycles.
- 1 <= queries.length <= 10^4
- 0 <= ui, vi <= numCourses - 1
- ui != vi
"""


class Solution:
    def checkIfPrerequisite(self, numCourses, prerequisites, queries):
        """
        Answer whether one course is a prerequisite of another.

        Args:
            numCourses: int - number of courses, labeled 0 to numCourses - 1
            prerequisites: List[List[int]] - prerequisites[i] = [a, b] means course b must be taken before course a
            queries: List[List[int]] - queries[j] = [u, v]

        Returns:
            List[bool] - answer[j] is True if queries[j][0] is a prerequisite of queries[j][1]

        Time Complexity: O(?)
        Space Complexity: O(?)
        """
        # TODO: Implement solution
        pass


# Example usage (for testing locally)
if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    result = solution.checkIfPrerequisite(2, [[1, 0]], [[0, 1], [1, 0]])
    print(f"Test 1: {result}")

    # Test case 2
    result = solution.checkIfPrerequisite(2, [], [[1, 0], [0, 1]])
    print(f"Test 2: {result}")
