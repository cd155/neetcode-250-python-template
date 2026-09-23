"""
Tests for LeetCode 23: Merge k Sorted Lists
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

# Import using importlib to avoid conflicts with built-in modules
import importlib.util
spec = importlib.util.spec_from_file_location("merge_k_sorted_lists", src_path / "linked_list" / "merge_k_sorted_lists.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
Solution = module.Solution
ListNode = module.ListNode


def build_linked_list(values):
    """Build a linked list from a list of values and return its head."""
    dummy = ListNode()
    tail = dummy
    for value in values:
        tail.next = ListNode(value)
        tail = tail.next
    return dummy.next


def linked_list_to_list(head):
    """Convert a linked list to a list of values."""
    values = []
    while head:
        values.append(head.val)
        head = head.next
    return values


class TestMergeKSortedLists:
    """Test cases for Merge k Sorted Lists problem"""

    def setup_method(self):
        """Setup test fixtures"""
        self.solution = Solution()

    def test_example_1(self):
        """Test case from example 1"""
        lists = [build_linked_list(values) for values in [[1, 4, 5], [1, 3, 4], [2, 6]]]
        result = self.solution.mergeKLists(lists)
        assert linked_list_to_list(result) == [1, 1, 2, 3, 4, 4, 5, 6]

    def test_example_2(self):
        """Test case from example 2"""
        lists = [build_linked_list(values) for values in []]
        result = self.solution.mergeKLists(lists)
        assert linked_list_to_list(result) == []

    def test_example_3(self):
        """Test case from example 3"""
        lists = [build_linked_list(values) for values in [[]]]
        result = self.solution.mergeKLists(lists)
        assert linked_list_to_list(result) == []
