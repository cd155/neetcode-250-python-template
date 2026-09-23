"""
LeetCode 297: Serialize and Deserialize Binary Tree

Serialization is the process of converting a data structure or object into a sequence of
bits so that it can be stored in a file or memory buffer, or transmitted across a
network connection link to be reconstructed later in the same or another computer
environment.

Design an algorithm to serialize and deserialize a binary tree. There is no restriction
on how your serialization/deserialization algorithm should work. You just need to ensure
that a binary tree can be serialized to a string and this string can be deserialized to
the original tree structure.

Clarification: The input/output format is the same as how LeetCode serializes a binary
tree. You do not necessarily need to follow this format, so please be creative and come
up with different approaches yourself.

Example 1:
Input: root = [1,2,3,null,null,4,5]
Output: [1,2,3,null,null,4,5]

Example 2:
Input: root = []
Output: []

Constraints:
- The number of nodes in the tree is in the range [0, 10^4].
- -1000 <= Node.val <= 1000
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Codec:
    def serialize(self, root):
        """
        Encode a tree to a single string.

        Args:
            root: Optional[TreeNode] - root of the binary tree

        Returns:
            str - serialized string

        Time Complexity: O(?)
        Space Complexity: O(?)
        """
        # TODO: Implement serialize
        pass

    def deserialize(self, data):
        """
        Decode the string back to a tree.

        Args:
            data: str - serialized string

        Returns:
            Optional[TreeNode] - root of the tree

        Time Complexity: O(?)
        Space Complexity: O(?)
        """
        # TODO: Implement deserialize
        pass


# Example usage (for testing locally)
if __name__ == "__main__":
    codec = Codec()

    # Test case 1
    root = TreeNode(1, TreeNode(2), TreeNode(3, TreeNode(4), TreeNode(5)))
    data = codec.serialize(root)
    result = codec.deserialize(data)
    print(f"Test 1: {data!r} -> root {result.val if result else None}")

    # Test case 2
    data = codec.serialize(None)
    print(f"Test 2: {data!r} -> {codec.deserialize(data)}")
