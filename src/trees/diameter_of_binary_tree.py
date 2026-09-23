"""
LeetCode 543: Diameter of Binary Tree

Given the root of a binary tree, return the length of the diameter of the tree.

The diameter of a binary tree is the length of the longest path between any two nodes in
a tree. This path may or may not pass through the root.

The length of a path between two nodes is represented by the number of edges between
them.

Example 1:
Input: root = [1,2,3,4,5]
Output: 3
Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].

Example 2:
Input: root = [1,2]
Output: 1

Constraints:
- The number of nodes in the tree is in the range [1, 10^4].
- -100 <= Node.val <= 100
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root):
        """
        Length of the longest path between any two nodes.

        Args:
            root: Optional[TreeNode] - root of the binary tree

        Returns:
            int - diameter (number of edges)

        Time Complexity: O(?)
        Space Complexity: O(?)
        """
        # TODO: Implement solution
        pass


# Example usage (for testing locally)
if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))
    result = solution.diameterOfBinaryTree(root)
    print(f"Test 1: {result}")

    # Test case 2
    root = TreeNode(1, TreeNode(2))
    result = solution.diameterOfBinaryTree(root)
    print(f"Test 2: {result}")
