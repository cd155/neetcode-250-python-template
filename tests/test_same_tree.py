"""
Tests for LeetCode 100: Same Tree
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
spec = importlib.util.spec_from_file_location("same_tree", src_path / "trees" / "same_tree.py")
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


class TestSameTree:
    """Test cases for Same Tree problem"""

    def setup_method(self):
        """Setup test fixtures"""
        self.solution = Solution()

    def test_example_1(self):
        """Test case from example 1"""
        p = build_tree([1, 2, 3])
        q = build_tree([1, 2, 3])
        result = self.solution.isSameTree(p, q)
        assert result is True

    def test_example_2(self):
        """Test case from example 2"""
        p = build_tree([1, 2])
        q = build_tree([1, None, 2])
        result = self.solution.isSameTree(p, q)
        assert result is False

    def test_example_3(self):
        """Test case from example 3"""
        p = build_tree([1, 2, 1])
        q = build_tree([1, 1, 2])
        result = self.solution.isSameTree(p, q)
        assert result is False
