"""
Tests for LeetCode 658: Find K Closest Elements
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

# Import using importlib to avoid conflicts with built-in modules
import importlib.util
spec = importlib.util.spec_from_file_location("find_k_closest_elements", src_path / "sliding_window" / "find_k_closest_elements.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
Solution = module.Solution


class TestFindKClosestElements:
    """Test cases for Find K Closest Elements problem"""

    def setup_method(self):
        """Setup test fixtures"""
        self.solution = Solution()

    def test_example_1(self):
        """Test case from example 1"""
        assert self.solution.findClosestElements([1, 2, 3, 4, 5], 4, 3) == [1, 2, 3, 4]

    def test_example_2(self):
        """Test case from example 2"""
        assert self.solution.findClosestElements([1, 1, 2, 3, 4, 5], 4, -1) == [1, 1, 2, 3]
