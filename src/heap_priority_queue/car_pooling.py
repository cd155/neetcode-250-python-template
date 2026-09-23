"""
LeetCode 1094: Car Pooling

There is a car with capacity empty seats. The vehicle only drives east (i.e., it cannot
turn around and drive west).

You are given the integer capacity and an array trips where trips[i] = [numPassengersi,
fromi, toi] indicates that the ith trip has numPassengersi passengers and the locations
to pick them up and drop them off are fromi and toi respectively. The locations are
given as the number of kilometers due east from the car's initial location.

Return true if it is possible to pick up and drop off all passengers for all the given
trips, or false otherwise.

Example 1:
Input: trips = [[2,1,5],[3,3,7]], capacity = 4
Output: false

Example 2:
Input: trips = [[2,1,5],[3,3,7]], capacity = 5
Output: true

Constraints:
- 1 <= trips.length <= 1000
- trips[i].length == 3
- 1 <= numPassengersi <= 100
- 0 <= fromi < toi <= 1000
- 1 <= capacity <= 10^5
"""


class Solution:
    def carPooling(self, trips, capacity):
        """
        Check whether all trips can be completed without exceeding capacity.

        Args:
            trips: List[List[int]] - trips[i] = [numPassengers, from, to]
            capacity: int - number of empty seats

        Returns:
            bool - True if every passenger can be picked up and dropped off

        Time Complexity: O(?)
        Space Complexity: O(?)
        """
        # TODO: Implement solution
        pass


# Example usage (for testing locally)
if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    result = solution.carPooling([[2, 1, 5], [3, 3, 7]], 4)
    print(f"Test 1: {result}")

    # Test case 2
    result = solution.carPooling([[2, 1, 5], [3, 3, 7]], 5)
    print(f"Test 2: {result}")
