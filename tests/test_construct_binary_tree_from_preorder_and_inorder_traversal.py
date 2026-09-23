"""
Tests for LeetCode 105: Construct Binary Tree from Preorder and Inorder Traversal
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
spec = importlib.util.spec_from_file_location("construct_binary_tree_from_preorder_and_inorder_traversal", src_path / "trees" / "construct_binary_tree_from_preorder_and_inorder_traversal.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
Solution = module.Solution
TreeNode = module.TreeNode


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


class TestConstructBinaryTreeFromPreorderAndInorderTraversal:
    """Test cases for Construct Binary Tree from Preorder and Inorder Traversal problem"""

    def setup_method(self):
        """Setup test fixtures"""
        self.solution = Solution()

    def test_example_1(self):
        """Test case from example 1"""
        result = self.solution.buildTree([3, 9, 20, 15, 7], [9, 3, 15, 20, 7])
        assert tree_to_list(result) == [3, 9, 20, None, None, 15, 7]

    def test_example_2(self):
        """Test case from example 2"""
        assert tree_to_list(self.solution.buildTree([-1], [-1])) == [-1]
