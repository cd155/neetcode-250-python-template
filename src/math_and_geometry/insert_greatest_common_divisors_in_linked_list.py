"""
LeetCode 2807: Insert Greatest Common Divisors in Linked List

Given the head of a linked list head, in which each node contains an integer value.

Between every pair of adjacent nodes, insert a new node with a value equal to the
greatest common divisor of them.

Return the linked list after insertion.

The greatest common divisor of two numbers is the largest positive integer that evenly
divides both numbers.

Example 1:
Input: head = [18,6,10,3]
Output: [18,6,6,2,10,1,3]
Explanation:
The 1st diagram denotes the initial linked list and the 2nd diagram denotes the linked
list after inserting the new nodes (nodes in blue are the inserted nodes).
- We insert the greatest common divisor of 18 and 6 = 6 between the 1st and the 2nd
nodes.
- We insert the greatest common divisor of 6 and 10 = 2 between the 2nd and the 3rd
nodes.
- We insert the greatest common divisor of 10 and 3 = 1 between the 3rd and the 4th
nodes.
There are no more adjacent nodes, so we return the linked list.

Example 2:
Input: head = [7]
Output: [7]
Explanation:
The 1st diagram denotes the initial linked list and the 2nd diagram denotes the linked
list after inserting the new nodes.
There are no pairs of adjacent nodes, so we return the initial linked list.

Constraints:
- The number of nodes in the list is in the range [1, 5000].
- 1 <= Node.val <= 1000
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def insertGreatestCommonDivisors(self, head):
        """
        Insert the GCD of every pair of adjacent nodes between them.

        Args:
            head: Optional[ListNode] - head of the linked list

        Returns:
            Optional[ListNode] - head of the updated list

        Time Complexity: O(?)
        Space Complexity: O(?)
        """
        # TODO: Implement solution
        pass


# Example usage (for testing locally)
if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    head = ListNode(18, ListNode(6, ListNode(10, ListNode(3))))
    result = solution.insertGreatestCommonDivisors(head)
    print(f"Test 1: {result.val if result else None}")

    # Test case 2
    head = ListNode(7)
    result = solution.insertGreatestCommonDivisors(head)
    print(f"Test 2: {result.val if result else None}")
