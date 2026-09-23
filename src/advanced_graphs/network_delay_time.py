"""
LeetCode 743: Network Delay Time

You are given a network of n nodes, labeled from 1 to n. You are also given times, a
list of travel times as directed edges times[i] = (ui, vi, wi), where ui is the source
node, vi is the target node, and wi is the time it takes for a signal to travel from
source to target.

We will send a signal from a given node k. Return the minimum time it takes for all the
n nodes to receive the signal. If it is impossible for all the n nodes to receive the
signal, return -1.

Example 1:
Input: times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2
Output: 2

Example 2:
Input: times = [[1,2,1]], n = 2, k = 1
Output: 1

Example 3:
Input: times = [[1,2,1]], n = 2, k = 2
Output: -1

Constraints:
- 1 <= k <= n <= 100
- 1 <= times.length <= 6000
- times[i].length == 3
- 1 <= ui, vi <= n
- ui != vi
- 0 <= wi <= 100
- All the pairs (ui, vi) are unique. (i.e., no multiple edges.)
"""


class Solution:
    def networkDelayTime(self, times, n, k):
        """
        Time for a signal from node k to reach every node.

        Args:
            times: List[List[int]] - times[i] = [u, v, w]: signal travel time w from node u to node v
            n: int - number of nodes, labeled 1 to n
            k: int - node that sends the signal

        Returns:
            int - minimum time, or -1

        Time Complexity: O(?)
        Space Complexity: O(?)
        """
        # TODO: Implement solution
        pass


# Example usage (for testing locally)
if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    result = solution.networkDelayTime([[2, 1, 1], [2, 3, 1], [3, 4, 1]], 4, 2)
    print(f"Test 1: {result}")

    # Test case 2
    result = solution.networkDelayTime([[1, 2, 1]], 2, 1)
    print(f"Test 2: {result}")
