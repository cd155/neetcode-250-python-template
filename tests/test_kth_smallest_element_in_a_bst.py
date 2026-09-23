"""
Tests for LeetCode 230: Kth Smallest Element in a BST
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
spec = importlib.util.spec_from_file_location("kth_smallest_element_in_a_bst", src_path / "trees" / "kth_smallest_element_in_a_bst.py")
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


class TestKthSmallestElementInABST:
    """Test cases for Kth Smallest Element in a BST problem"""

    def setup_method(self):
        """Setup test fixtures"""
        self.solution = Solution()

    def test_example_1(self):
        """Test case from example 1"""
        root = build_tree([3, 1, 4, None, 2])
        result = self.solution.kthSmallest(root, 1)
        assert result == 1

    def test_example_2(self):
        """Test case from example 2"""
        root = build_tree([5, 3, 6, 2, 4, None, None, 1])
        result = self.solution.kthSmallest(root, 3)
        assert result == 3
