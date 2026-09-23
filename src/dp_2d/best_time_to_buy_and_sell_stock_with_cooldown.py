"""
LeetCode 309: Best Time to Buy and Sell Stock with Cooldown

You are given an array prices where prices[i] is the price of a given stock on the ith
day.

Find the maximum profit you can achieve. You may complete as many transactions as you
like (i.e., buy one and sell one share of the stock multiple times) with the following
restrictions:

- After you sell your stock, you cannot buy stock on the next day (i.e., cooldown one
  day).

Note: You may not engage in multiple transactions simultaneously (i.e., you must sell
the stock before you buy again).

Example 1:
Input: prices = [1,2,3,0,2]
Output: 3
Explanation: transactions = [buy, sell, cooldown, buy, sell]

Example 2:
Input: prices = [1]
Output: 0

Constraints:
- 1 <= prices.length <= 5000
- 0 <= prices[i] <= 1000
"""


class Solution:
    def maxProfit(self, prices):
        """
        Maximum profit with a one-day cooldown after selling.

        Args:
            prices: List[int] - prices[i] is the price of the stock on day i

        Returns:
            int - maximum profit

        Time Complexity: O(?)
        Space Complexity: O(?)
        """
        # TODO: Implement solution
        pass


# Example usage (for testing locally)
if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    result = solution.maxProfit([1, 2, 3, 0, 2])
    print(f"Test 1: {result}")

    # Test case 2
    result = solution.maxProfit([1])
    print(f"Test 2: {result}")
