"""
Tests for LeetCode 2807: Insert Greatest Common Divisors in Linked List
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

# Import using importlib to avoid conflicts with built-in modules
import importlib.util
spec = importlib.util.spec_from_file_location("insert_greatest_common_divisors_in_linked_list", src_path / "math_and_geometry" / "insert_greatest_common_divisors_in_linked_list.py")
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


class TestInsertGreatestCommonDivisorsInLinkedList:
    """Test cases for Insert Greatest Common Divisors in Linked List problem"""

    def setup_method(self):
        """Setup test fixtures"""
        self.solution = Solution()

    def test_example_1(self):
        """Test case from example 1"""
        head = build_linked_list([18, 6, 10, 3])
        result = self.solution.insertGreatestCommonDivisors(head)
        assert linked_list_to_list(result) == [18, 6, 6, 2, 10, 1, 3]

    def test_example_2(self):
        """Test case from example 2"""
        head = build_linked_list([7])
        result = self.solution.insertGreatestCommonDivisors(head)
        assert linked_list_to_list(result) == [7]
