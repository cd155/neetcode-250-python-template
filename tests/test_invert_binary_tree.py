"""
Tests for LeetCode 226: Invert Binary Tree
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
spec = importlib.util.spec_from_file_location("invert_binary_tree", src_path / "trees" / "invert_binary_tree.py")
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


def tree_to_list(root):
    """Convert a binary tree to its level-order list, dropping trailing None values."""
    values = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node:
            values.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            values.append(None)
    while values and values[-1] is None:
        values.pop()
    return values


class TestInvertBinaryTree:
    """Test cases for Invert Binary Tree problem"""

    def setup_method(self):
        """Setup test fixtures"""
        self.solution = Solution()

    def test_example_1(self):
        """Test case from example 1"""
        root = build_tree([4, 2, 7, 1, 3, 6, 9])
        result = self.solution.invertTree(root)
        assert tree_to_list(result) == [4, 7, 2, 9, 6, 3, 1]

    def test_example_2(self):
        """Test case from example 2"""
        root = build_tree([2, 1, 3])
        result = self.solution.invertTree(root)
        assert tree_to_list(result) == [2, 3, 1]

    def test_example_3(self):
        """Test case from example 3"""
        root = build_tree([])
        result = self.solution.invertTree(root)
        assert tree_to_list(result) == []
