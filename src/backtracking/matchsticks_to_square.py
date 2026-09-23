"""
LeetCode 473: Matchsticks to Square

You are given an integer array matchsticks where matchsticks[i] is the length of the ith
matchstick. You want to use all the matchsticks to make one square. You should not break
any stick, but you can link them up, and each matchstick must be used exactly one time.

Return true if you can make this square and false otherwise.

Example 1:
Input: matchsticks = [1,1,2,2,2]
Output: true
Explanation:
You can form a square with length 2, one side of the square came two sticks with length
1.

Example 2:
Input: matchsticks = [3,3,3,3,4]
Output: false
Explanation: You cannot find a way to form a square with all the matchsticks.

Constraints:
- 1 <= matchsticks.length <= 15
- 1 <= matchsticks[i] <= 10^8
"""


class Solution:
    def makesquare(self, matchsticks):
        """
        Check whether all matchsticks can form a square.

        Args:
            matchsticks: List[int] - matchsticks[i] is the length of the i-th matchstick

        Returns:
            bool - True if a square can be made

        Time Complexity: O(?)
        Space Complexity: O(?)
        """
        # TODO: Implement solution
        pass


# Example usage (for testing locally)
if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    result = solution.makesquare([1, 1, 2, 2, 2])
    print(f"Test 1: {result}")

    # Test case 2
    result = solution.makesquare([3, 3, 3, 3, 4])
    print(f"Test 2: {result}")
