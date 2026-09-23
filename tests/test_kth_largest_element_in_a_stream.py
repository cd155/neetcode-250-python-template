"""
Tests for LeetCode 703: Kth Largest Element in a Stream
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

# Import using importlib to avoid conflicts with built-in modules
import importlib.util
spec = importlib.util.spec_from_file_location("kth_largest_element_in_a_stream", src_path / "heap_priority_queue" / "kth_largest_element_in_a_stream.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
KthLargest = module.KthLargest


class TestKthLargestElementInAStream:
    """Test cases for Kth Largest Element in a Stream problem"""

    def test_example_1(self):
        """Test case from example 1"""
        kthLargest = KthLargest(3, [4, 5, 8, 2])
        assert kthLargest.add(3) == 4
        assert kthLargest.add(5) == 5
        assert kthLargest.add(10) == 5
        assert kthLargest.add(9) == 8
        assert kthLargest.add(4) == 8

    def test_example_2(self):
        """Test case from example 2"""
        kthLargest = KthLargest(4, [7, 7, 7, 7, 8, 3])
        assert kthLargest.add(2) == 7
        assert kthLargest.add(10) == 7
        assert kthLargest.add(9) == 7
        assert kthLargest.add(9) == 8
