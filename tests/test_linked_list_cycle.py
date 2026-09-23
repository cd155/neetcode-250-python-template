"""
Tests for LeetCode 141: Linked List Cycle
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

# Import using importlib to avoid conflicts with built-in modules
import importlib.util
spec = importlib.util.spec_from_file_location("linked_list_cycle", src_path / "linked_list" / "linked_list_cycle.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
Solution = module.Solution
ListNode = module.ListNode


def build_linked_list_with_cycle(values, pos):
    """Build a linked list whose tail links to the node at index pos (-1 means no cycle)."""
    nodes = [ListNode(value) for value in values]
    for current, following in zip(nodes, nodes[1:]):
        current.next = following
    if nodes and pos != -1:
        nodes[-1].next = nodes[pos]
    return nodes[0] if nodes else None


class TestLinkedListCycle:
    """Test cases for Linked List Cycle problem"""

    def setup_method(self):
        """Setup test fixtures"""
        self.solution = Solution()

    def test_example_1(self):
        """Test case from example 1"""
        head = build_linked_list_with_cycle([3, 2, 0, -4], 1)
        assert self.solution.hasCycle(head) is True

    def test_example_2(self):
        """Test case from example 2"""
        head = build_linked_list_with_cycle([1, 2], 0)
        assert self.solution.hasCycle(head) is True

    def test_example_3(self):
        """Test case from example 3"""
        head = build_linked_list_with_cycle([1], -1)
        assert self.solution.hasCycle(head) is False
