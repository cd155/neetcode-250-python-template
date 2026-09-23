"""
LeetCode 94: Binary Tree Inorder Traversal

Given the root of a binary tree, return the inorder traversal of its nodes' values.

Example 1:
Input: root = [1,null,2,3]
Output: [1,3,2]

Example 2:
Input: root = [1,2,3,4,5,null,8,null,null,6,7,9]
Output: [4,2,6,5,7,1,3,9,8]

Example 3:
Input: root = []
Output: []

Example 4:
Input: root = [1]
Output: [1]

Constraints:
- The number of nodes in the tree is in the range [0, 100].
- -100 <= Node.val <= 100

Follow up: Recursive solution is trivial, could you do it iteratively?
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root):
        """
        Inorder traversal of a binary tree.

        Args:
            root: Optional[TreeNode] - root of the binary tree

        Returns:
            List[int] - node values in inorder

        Time Complexity: O(?)
        Space Complexity: O(?)
        """
        # TODO: Implement solution
        pass


# Example usage (for testing locally)
if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    root = TreeNode(1, None, TreeNode(2, TreeNode(3)))
    result = solution.inorderTraversal(root)
    print(f"Test 1: {result}")

    # Test case 2
    root = TreeNode(
        1,
        TreeNode(2, TreeNode(4), TreeNode(5, TreeNode(6), TreeNode(7))),
        TreeNode(3, None, TreeNode(8, TreeNode(9))),
    )
    result = solution.inorderTraversal(root)
    print(f"Test 2: {result}")
