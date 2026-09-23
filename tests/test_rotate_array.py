"""
Tests for LeetCode 189: Rotate Array
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

# Import using importlib to avoid conflicts with built-in modules
import importlib.util
spec = importlib.util.spec_from_file_location("rotate_array", src_path / "two_pointers" / "rotate_array.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
Solution = module.Solution


class TestRotateArray:
    """Test cases for Rotate Array problem"""

    def setup_method(self):
        """Setup test fixtures"""
        self.solution = Solution()

    def test_example_1(self):
        """Test case from example 1"""
        nums = [1, 2, 3, 4, 5, 6, 7]
        self.solution.rotate(nums, 3)
        assert nums == [5, 6, 7, 1, 2, 3, 4]

    def test_example_2(self):
        """Test case from example 2"""
        nums = [-1, -100, 3, 99]
        self.solution.rotate(nums, 2)
        assert nums == [3, 99, -1, -100]
