"""
Tests for LeetCode 75: Sort Colors
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

# Import using importlib to avoid conflicts with built-in modules
import importlib.util
spec = importlib.util.spec_from_file_location("sort_colors", src_path / "arrays_and_hashing" / "sort_colors.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
Solution = module.Solution


class TestSortColors:
    """Test cases for Sort Colors problem"""

    def setup_method(self):
        """Setup test fixtures"""
        self.solution = Solution()

    def test_example_1(self):
        """Test case from example 1"""
        nums = [2, 0, 2, 1, 1, 0]
        self.solution.sortColors(nums)
        assert nums == [0, 0, 1, 1, 2, 2]

    def test_example_2(self):
        """Test case from example 2"""
        nums = [2, 0, 1]
        self.solution.sortColors(nums)
        assert nums == [0, 1, 2]
