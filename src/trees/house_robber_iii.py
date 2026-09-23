"""
LeetCode 337: House Robber III

The thief has found himself a new place for his thievery again. There is only one
entrance to this area, called root.

Besides the root, each house has one and only one parent house. After a tour, the smart
thief realized that all houses in this place form a binary tree. It will automatically
contact the police if two directly-linked houses were broken into on the same night.

Given the root of the binary tree, return the maximum amount of money the thief can rob
without alerting the police.

Example 1:
Input: root = [3,2,3,null,3,null,1]
Output: 7
Explanation: Maximum amount of money the thief can rob = 3 + 3 + 1 = 7.

Example 2:
Input: root = [3,4,5,1,3,null,1]
Output: 9
Explanation: Maximum amount of money the thief can rob = 4 + 5 = 9.

Constraints:
- The number of nodes in the tree is in the range [1, 10^4].
- 0 <= Node.val <= 10^4
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rob(self, root):
        """
        Maximum amount the thief can rob without robbing two directly-linked houses.

        Args:
            root: Optional[TreeNode] - root of the binary tree of houses

        Returns:
            int - maximum amount of money

        Time Complexity: O(?)
        Space Complexity: O(?)
        """
        # TODO: Implement solution
        pass


# Example usage (for testing locally)
if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    root = TreeNode(3, TreeNode(2, None, TreeNode(3)), TreeNode(3, None, TreeNode(1)))
    result = solution.rob(root)
    print(f"Test 1: {result}")

    # Test case 2
    root = TreeNode(3, TreeNode(4, TreeNode(1), TreeNode(3)), TreeNode(5, None, TreeNode(1)))
    result = solution.rob(root)
    print(f"Test 2: {result}")
