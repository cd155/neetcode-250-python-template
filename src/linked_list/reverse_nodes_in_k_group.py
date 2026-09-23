"""
LeetCode 25: Reverse Nodes in k-Group

Given the head of a linked list, reverse the nodes of the list k at a time, and return
the modified list.

k is a positive integer and is less than or equal to the length of the linked list. If
the number of nodes is not a multiple of k then left-out nodes, in the end, should
remain as it is.

You may not alter the values in the list's nodes, only nodes themselves may be changed.

Example 1:
Input: head = [1,2,3,4,5], k = 2
Output: [2,1,4,3,5]

Example 2:
Input: head = [1,2,3,4,5], k = 3
Output: [3,2,1,4,5]

Constraints:
- The number of nodes in the list is n.
- 1 <= k <= n <= 5000
- 0 <= Node.val <= 1000

Follow-up: Can you solve the problem in O(1) extra memory space?
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head, k):
        """
        Reverse the nodes of the list k at a time.

        Args:
            head: Optional[ListNode] - head of the linked list
            k: int - group size

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
    result = solution.reverseKGroup(head, 2)
    print(f"Test 1: {result.val if result else None}")

    # Test case 2
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    result = solution.reverseKGroup(head, 3)
    print(f"Test 2: {result.val if result else None}")
