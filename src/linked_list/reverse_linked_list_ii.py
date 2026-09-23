"""
LeetCode 92: Reverse Linked List II

Given the head of a singly linked list and two integers left and right where left <=
right, reverse the nodes of the list from position left to position right, and return
the reversed list.

Example 1:
Input: head = [1,2,3,4,5], left = 2, right = 4
Output: [1,4,3,2,5]

Example 2:
Input: head = [5], left = 1, right = 1
Output: [5]

Constraints:
- The number of nodes in the list is n.
- 1 <= n <= 500
- -500 <= Node.val <= 500
- 1 <= left <= right <= n

Follow up: Could you do it in one pass?
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head, left, right):
        """
        Reverse the nodes from position left to position right.

        Args:
            head: Optional[ListNode] - head of the linked list
            left: int - start position (1-indexed)
            right: int - end position (1-indexed)

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
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    result = solution.reverseBetween(head, 2, 4)
    print(f"Test 1: {result.val if result else None}")

    # Test case 2
    head = ListNode(5)
    result = solution.reverseBetween(head, 1, 1)
    print(f"Test 2: {result.val if result else None}")
