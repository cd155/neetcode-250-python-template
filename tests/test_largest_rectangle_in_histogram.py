"""
Tests for LeetCode 84: Largest Rectangle in Histogram
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

# Import using importlib to avoid conflicts with built-in modules
import importlib.util
spec = importlib.util.spec_from_file_location("largest_rectangle_in_histogram", src_path / "stack" / "largest_rectangle_in_histogram.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
Solution = module.Solution


class TestLargestRectangleInHistogram:
    """Test cases for Largest Rectangle in Histogram problem"""

    def setup_method(self):
        """Setup test fixtures"""
        self.solution = Solution()

    def test_example_1(self):
        """Test case from example 1"""
        assert self.solution.largestRectangleArea([2, 1, 5, 6, 2, 3]) == 10

    def test_example_2(self):
        """Test case from example 2"""
        assert self.solution.largestRectangleArea([2, 4]) == 4
