"""
Tests for LeetCode 94: Binary Tree Inorder Traversal
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
spec = importlib.util.spec_from_file_location("binary_tree_inorder_traversal", src_path / "trees" / "binary_tree_inorder_traversal.py")
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


class TestBinaryTreeInorderTraversal:
    """Test cases for Binary Tree Inorder Traversal problem"""

    def setup_method(self):
        """Setup test fixtures"""
        self.solution = Solution()

    def test_example_1(self):
        """Test case from example 1"""
        root = build_tree([1, None, 2, 3])
        result = self.solution.inorderTraversal(root)
        assert result == [1, 3, 2]

    def test_example_2(self):
        """Test case from example 2"""
        root = build_tree([1, 2, 3, 4, 5, None, 8, None, None, 6, 7, 9])
        result = self.solution.inorderTraversal(root)
        assert result == [4, 2, 6, 5, 7, 1, 3, 9, 8]

    def test_example_3(self):
        """Test case from example 3"""
        root = build_tree([])
        result = self.solution.inorderTraversal(root)
        assert result == []

    def test_example_4(self):
        """Test case from example 4"""
        root = build_tree([1])
        result = self.solution.inorderTraversal(root)
        assert result == [1]
