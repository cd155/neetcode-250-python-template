"""
LeetCode 138: Copy List with Random Pointer

A linked list of length n is given such that each node contains an additional random
pointer, which could point to any node in the list, or null.

Construct a deep copy of the list. The deep copy should consist of exactly n brand new
nodes, where each new node has its value set to the value of its corresponding original
node. Both the next and random pointer of the new nodes should point to new nodes in the
copied list such that the pointers in the original list and copied list represent the
same list state. None of the pointers in the new list should point to nodes in the
original list.

For example, if there are two nodes X and Y in the original list, where X.random --> Y,
then for the corresponding two nodes x and y in the copied list, x.random --> y.

Return the head of the copied linked list.

The linked list is represented in the input/output as a list of n nodes. Each node is
represented as a pair of [val, random_index] where:

- val: an integer representing Node.val
- random_index: the index of the node (range from 0 to n-1) that the random pointer
  points to, or null if it does not point to any node.

Your code will only be given the head of the original linked list.

Example 1:
Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]

Example 2:
Input: head = [[1,1],[2,1]]
Output: [[1,1],[2,1]]

Example 3:
Input: head = [[3,null],[3,0],[3,null]]
Output: [[3,null],[3,0],[3,null]]

Constraints:
- 0 <= n <= 1000
- -10^4 <= Node.val <= 10^4
- Node.random is null or is pointing to some node in the linked list.
"""


class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head):
        """
        Deep copy a linked list whose nodes also have a random pointer.

        Args:
            head: Optional[Node] - head of the linked list

        Returns:
            Optional[Node] - head of the copied list

        Time Complexity: O(?)
        Space Complexity: O(?)
        """
        # TODO: Implement solution
        pass


# Example usage (for testing locally)
if __name__ == "__main__":
    solution = Solution()

    # Test case 1: [[7,null],[13,0],[11,4],[10,2],[1,0]]
    nodes = [Node(7), Node(13), Node(11), Node(10), Node(1)]
    for current, following in zip(nodes, nodes[1:]):
        current.next = following
    for node, random_index in zip(nodes, [None, 0, 4, 2, 0]):
        node.random = nodes[random_index] if random_index is not None else None
    result = solution.copyRandomList(nodes[0])
    print(f"Test 1: {result.val if result else None}")

    # Test case 2: [[1,1],[2,1]]
    nodes = [Node(1), Node(2)]
    nodes[0].next = nodes[1]
    nodes[0].random = nodes[1]
    nodes[1].random = nodes[1]
    result = solution.copyRandomList(nodes[0])
    print(f"Test 2: {result.val if result else None}")
