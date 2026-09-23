"""
LeetCode 141: Linked List Cycle

Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached
again by continuously following the next pointer. Internally, pos is used to denote the
index of the node that tail's next pointer is connected to. Note that pos is not passed
as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.

Example 1:
Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation:
There is a cycle in the linked list, where the tail connects to the 1st node
(0-indexed).

Example 2:
Input: head = [1,2], pos = 0
Output: true
Explanation:
There is a cycle in the linked list, where the tail connects to the 0th node.

Example 3:
Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.

Constraints:
- The number of the nodes in the list is in the range [0, 10^4].
- -10^5 <= Node.val <= 10^5
- pos is -1 or a valid index in the linked-list.

Follow up: Can you solve it using O(1) (i.e. constant) memory?
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def hasCycle(self, head):
        """
        Determine whether the linked list has a cycle.

        Args:
            head: Optional[ListNode] - head of the linked list

        Returns:
            bool - True if there is a cycle

        Time Complexity: O(?)
        Space Complexity: O(?)
        """
        # TODO: Implement solution
        pass


# Example usage (for testing locally)
if __name__ == "__main__":
    solution = Solution()

    # Test case 1: 3 -> 2 -> 0 -> -4, and -4 links back to 2
    nodes = [ListNode(3), ListNode(2), ListNode(0), ListNode(-4)]
    for current, following in zip(nodes, nodes[1:]):
        current.next = following
    nodes[-1].next = nodes[1]
    result = solution.hasCycle(nodes[0])
    print(f"Test 1: {result}")

    # Test case 2: 1 -> 2, and 2 links back to 1
    nodes = [ListNode(1), ListNode(2)]
    nodes[0].next = nodes[1]
    nodes[1].next = nodes[0]
    result = solution.hasCycle(nodes[0])
    print(f"Test 2: {result}")
