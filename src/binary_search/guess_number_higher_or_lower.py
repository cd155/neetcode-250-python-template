"""
LeetCode 374: Guess Number Higher or Lower

We are playing the Guess Game. The game is as follows:

I pick a number from 1 to n. You have to guess which number I picked (the number I
picked stays the same throughout the game).

Every time you guess wrong, I will tell you whether the number I picked is higher or
lower than your guess.

You call a pre-defined API int guess(int num), which returns three possible results:

- -1: Your guess is higher than the number I picked (i.e. num > pick).
- 1: Your guess is lower than the number I picked (i.e. num < pick).
- 0: your guess is equal to the number I picked (i.e. num == pick).

Return the number that I picked.

Example 1:
Input: n = 10, pick = 6
Output: 6

Example 2:
Input: n = 1, pick = 1
Output: 1

Example 3:
Input: n = 2, pick = 1
Output: 1

Constraints:
- 1 <= n <= 2^31 - 1
- 1 <= pick <= n
"""


# The guess API is predefined on LeetCode. This local version compares against
# the module-level `pick`, so set `pick` before calling guessNumber.
pick = 6


def guess(num):
    """
    Compare num with the picked number.

    Args:
        num: int - your guess

    Returns:
        int - -1 if num > pick, 1 if num < pick, 0 if num == pick
    """
    if num > pick:
        return -1
    if num < pick:
        return 1
    return 0


class Solution:
    def guessNumber(self, n):
        """
        Find the picked number using the guess API.

        Args:
            n: int - the number is picked from 1 to n

        Returns:
            int - the picked number

        Time Complexity: O(?)
        Space Complexity: O(?)
        """
        # TODO: Implement solution
        pass


# Example usage (for testing locally)
if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    pick = 6
    result = solution.guessNumber(10)
    print(f"Test 1: {result}")

    # Test case 2
    pick = 1
    result = solution.guessNumber(1)
    print(f"Test 2: {result}")
