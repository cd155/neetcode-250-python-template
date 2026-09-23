"""
Tests for LeetCode 297: Serialize and Deserialize Binary Tree
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
spec = importlib.util.spec_from_file_location("serialize_and_deserialize_binary_tree", src_path / "trees" / "serialize_and_deserialize_binary_tree.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
Codec = module.Codec
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


class TestSerializeAndDeserializeBinaryTree:
    """Test cases for Serialize and Deserialize Binary Tree problem"""

    def test_example_1(self):
        """Test case from example 1"""
        codec = Codec()
        root = build_tree([1, 2, 3, None, None, 4, 5])
        data = codec.serialize(root)
        assert isinstance(data, str)
        assert tree_to_list(codec.deserialize(data)) == [1, 2, 3, None, None, 4, 5]

    def test_example_2(self):
        """Test case from example 2"""
        codec = Codec()
        data = codec.serialize(None)
        assert isinstance(data, str)
        assert codec.deserialize(data) is None
