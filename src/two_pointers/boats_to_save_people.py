"""
LeetCode 881: Boats to Save People

You are given an array people where people[i] is the weight of the ith person, and an
infinite number of boats where each boat can carry a maximum weight of limit. Each boat
carries at most two people at the same time, provided the sum of the weight of those
people is at most limit.

Return the minimum number of boats to carry every given person.

Example 1:
Input: people = [1,2], limit = 3
Output: 1
Explanation: 1 boat (1, 2)

Example 2:
Input: people = [3,2,2,1], limit = 3
Output: 3
Explanation: 3 boats (1, 2), (2) and (3)

Example 3:
Input: people = [3,5,3,4], limit = 5
Output: 4
Explanation: 4 boats (3), (3), (4), (5)

Constraints:
- 1 <= people.length <= 5 * 10^4
- 1 <= people[i] <= limit <= 3 * 10^4
"""


class Solution:
    def numRescueBoats(self, people, limit):
        """
        Minimum number of boats (each holds at most two people) to carry everyone.

        Args:
            people: List[int] - people[i] is the weight of the i-th person
            limit: int - maximum weight a boat can carry

        Returns:
            int - minimum number of boats

        Time Complexity: O(?)
        Space Complexity: O(?)
        """
        # TODO: Implement solution
        pass


# Example usage (for testing locally)
if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    result = solution.numRescueBoats([1, 2], 3)
    print(f"Test 1: {result}")

    # Test case 2
    result = solution.numRescueBoats([3, 2, 2, 1], 3)
    print(f"Test 2: {result}")
