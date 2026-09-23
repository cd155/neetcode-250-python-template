"""
Tests for LeetCode 136: Single Number
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

# Import using importlib to avoid conflicts with built-in modules
import importlib.util
spec = importlib.util.spec_from_file_location("single_number", src_path / "bit_manipulation" / "single_number.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
Solution = module.Solution


class TestSingleNumber:
    """Test cases for Single Number problem"""

    def setup_method(self):
        """Setup test fixtures"""
        self.solution = Solution()

    def test_example_1(self):
        """Test case from example 1"""
        assert self.solution.singleNumber([2, 2, 1]) == 1

    def test_example_2(self):
        """Test case from example 2"""
        assert self.solution.singleNumber([4, 1, 2, 1, 2]) == 4

    def test_example_3(self):
        """Test case from example 3"""
        assert self.solution.singleNumber([1]) == 1
