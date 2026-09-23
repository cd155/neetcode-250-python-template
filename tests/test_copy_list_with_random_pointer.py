"""
Tests for LeetCode 138: Copy List with Random Pointer
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

# Import using importlib to avoid conflicts with built-in modules
import importlib.util
spec = importlib.util.spec_from_file_location("copy_list_with_random_pointer", src_path / "linked_list" / "copy_list_with_random_pointer.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
Solution = module.Solution
Node = module.Node


def build_random_list(pairs):
    """Build a list from [val, random_index] pairs and return its head."""
    nodes = [Node(val) for val, _ in pairs]
    for current, following in zip(nodes, nodes[1:]):
        current.next = following
    for node, (_, random_index) in zip(nodes, pairs):
        node.random = nodes[random_index] if random_index is not None else None
    return nodes[0] if nodes else None


def list_nodes(head):
    """Return the nodes of the list in order."""
    nodes = []
    while head:
        nodes.append(head)
        head = head.next
    return nodes


def random_list_to_pairs(head):
    """Convert a list to [val, random_index] pairs; random pointers outside the list show as "outside"."""
    nodes = list_nodes(head)
    index = {id(node): i for i, node in enumerate(nodes)}
    return [[node.val, index.get(id(node.random), "outside") if node.random else None] for node in nodes]


def shares_nodes(head1, head2):
    """Check whether two lists share any node object."""
    ids = {id(node) for node in list_nodes(head1)}
    return any(id(node) in ids for node in list_nodes(head2))


class TestCopyListWithRandomPointer:
    """Test cases for Copy List with Random Pointer problem"""

    def setup_method(self):
        """Setup test fixtures"""
        self.solution = Solution()

    def test_example_1(self):
        """Test case from example 1"""
        head = build_random_list([[7, None], [13, 0], [11, 4], [10, 2], [1, 0]])
        result = self.solution.copyRandomList(head)
        assert random_list_to_pairs(result) == [[7, None], [13, 0], [11, 4], [10, 2], [1, 0]]
        assert not shares_nodes(head, result)

    def test_example_2(self):
        """Test case from example 2"""
        head = build_random_list([[1, 1], [2, 1]])
        result = self.solution.copyRandomList(head)
        assert random_list_to_pairs(result) == [[1, 1], [2, 1]]
        assert not shares_nodes(head, result)

    def test_example_3(self):
        """Test case from example 3"""
        head = build_random_list([[3, None], [3, 0], [3, None]])
        result = self.solution.copyRandomList(head)
        assert random_list_to_pairs(result) == [[3, None], [3, 0], [3, None]]
        assert not shares_nodes(head, result)
