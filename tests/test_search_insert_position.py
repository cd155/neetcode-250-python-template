"""
Tests for LeetCode 35: Search Insert Position
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

# Import using importlib to avoid conflicts with built-in modules
import importlib.util
spec = importlib.util.spec_from_file_location("search_insert_position", src_path / "binary_search" / "search_insert_position.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
Solution = module.Solution


class TestSearchInsertPosition:
    """Test cases for Search Insert Position problem"""

    def setup_method(self):
        """Setup test fixtures"""
        self.solution = Solution()

    def test_example_1(self):
        """Test case from example 1"""
        assert self.solution.searchInsert([1, 3, 5, 6], 5) == 2

    def test_example_2(self):
        """Test case from example 2"""
        assert self.solution.searchInsert([1, 3, 5, 6], 2) == 1

    def test_example_3(self):
        """Test case from example 3"""
        assert self.solution.searchInsert([1, 3, 5, 6], 7) == 4
