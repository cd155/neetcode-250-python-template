"""
LeetCode 1584: Min Cost to Connect All Points

You are given an array points representing integer coordinates of some points on a
2D-plane, where points[i] = [xi, yi].

The cost of connecting two points [xi, yi] and [xj, yj] is the manhattan distance
between them: |xi - xj| + |yi - yj|, where |val| denotes the absolute value of val.

Return the minimum cost to make all points connected. All points are connected if there
is exactly one simple path between any two points.

Example 1:
Input: points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
Output: 20
Explanation:
We can connect the points as shown above to get the minimum cost of 20.
Notice that there is a unique path between every pair of points.

Example 2:
Input: points = [[3,12],[-2,5],[-4,1]]
Output: 18

Constraints:
- 1 <= points.length <= 1000
- -10^6 <= xi, yi <= 10^6
- All pairs (xi, yi) are distinct.
"""


class Solution:
    def minCostConnectPoints(self, points):
        """
        Minimum cost to connect all points (Manhattan distance).

        Args:
            points: List[List[int]] - list of [x, y] points

        Returns:
            int - minimum cost

        Time Complexity: O(?)
        Space Complexity: O(?)
        """
        # TODO: Implement solution
        pass


# Example usage (for testing locally)
if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    points = [[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]]
    result = solution.minCostConnectPoints(points)
    print(f"Test 1: {result}")

    # Test case 2
    result = solution.minCostConnectPoints([[3, 12], [-2, 5], [-4, 1]])
    print(f"Test 2: {result}")
