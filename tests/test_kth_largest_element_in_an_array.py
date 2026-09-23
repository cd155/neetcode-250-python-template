"""
Tests for LeetCode 215: Kth Largest Element in an Array
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

# Import using importlib to avoid conflicts with built-in modules
import importlib.util
spec = importlib.util.spec_from_file_location("kth_largest_element_in_an_array", src_path / "heap_priority_queue" / "kth_largest_element_in_an_array.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
Solution = module.Solution


class TestKthLargestElementInAnArray:
    """Test cases for Kth Largest Element in an Array problem"""

    def setup_method(self):
        """Setup test fixtures"""
        self.solution = Solution()

    def test_example_1(self):
        """Test case from example 1"""
        assert self.solution.findKthLargest([3, 2, 1, 5, 6, 4], 2) == 5

    def test_example_2(self):
        """Test case from example 2"""
        assert self.solution.findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4) == 4
