"""
Tests for LeetCode 2: Add Two Numbers
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

# Import using importlib to avoid conflicts with built-in modules
import importlib.util
spec = importlib.util.spec_from_file_location("add_two_numbers", src_path / "linked_list" / "add_two_numbers.py")
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


class TestAddTwoNumbers:
    """Test cases for Add Two Numbers problem"""

    def setup_method(self):
        """Setup test fixtures"""
        self.solution = Solution()

    def test_example_1(self):
        """Test case from example 1"""
        l1 = build_linked_list([2, 4, 3])
        l2 = build_linked_list([5, 6, 4])
        result = self.solution.addTwoNumbers(l1, l2)
        assert linked_list_to_list(result) == [7, 0, 8]

    def test_example_2(self):
        """Test case from example 2"""
        l1 = build_linked_list([0])
        l2 = build_linked_list([0])
        result = self.solution.addTwoNumbers(l1, l2)
        assert linked_list_to_list(result) == [0]

    def test_example_3(self):
        """Test case from example 3"""
        l1 = build_linked_list([9, 9, 9, 9, 9, 9, 9])
        l2 = build_linked_list([9, 9, 9, 9])
        result = self.solution.addTwoNumbers(l1, l2)
        assert linked_list_to_list(result) == [8, 9, 9, 9, 0, 0, 0, 1]
