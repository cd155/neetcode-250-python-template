"""
Tests for LeetCode 450: Delete Node in a BST
"""

import pytest
import sys
from collections import deque
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

# Import using importlib to avoid conflicts with built-in modules
import importlib.util
spec = importlib.util.spec_from_file_location("delete_node_in_a_bst", src_path / "trees" / "delete_node_in_a_bst.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
Solution = module.Solution
TreeNode = module.TreeNode


def build_tree(values):
    """Build a binary tree from its level-order list (None marks a missing node)."""
    if not values or values[0] is None:
        return None
    root = TreeNode(values[0])
    queue = deque([root])
    i = 1
    while queue and i < len(values):
        node = queue.popleft()
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1
    return root


def inorder_values(root):
    """Return the values of the tree in inorder (sorted for a valid BST)."""
    if not root:
        return []
    return inorder_values(root.left) + [root.val] + inorder_values(root.right)


class TestDeleteNodeInABST:
    """Test cases for Delete Node in a BST problem"""

    def setup_method(self):
        """Setup test fixtures"""
        self.solution = Solution()

    def test_example_1(self):
        """Test case from example 1 (any valid BST is accepted)"""
        root = build_tree([5, 3, 6, 2, 4, None, 7])
        result = self.solution.deleteNode(root, 3)
        assert inorder_values(result) == [2, 4, 5, 6, 7]

    def test_example_2(self):
        """Test case from example 2"""
        root = build_tree([5, 3, 6, 2, 4, None, 7])
        result = self.solution.deleteNode(root, 0)
        assert inorder_values(result) == [2, 3, 4, 5, 6, 7]

    def test_example_3(self):
        """Test case from example 3"""
        assert self.solution.deleteNode(None, 0) is None
