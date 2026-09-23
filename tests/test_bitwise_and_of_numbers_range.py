"""
Tests for LeetCode 201: Bitwise AND of Numbers Range
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

# Import using importlib to avoid conflicts with built-in modules
import importlib.util
spec = importlib.util.spec_from_file_location("bitwise_and_of_numbers_range", src_path / "bit_manipulation" / "bitwise_and_of_numbers_range.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
Solution = module.Solution


class TestBitwiseAndOfNumbersRange:
    """Test cases for Bitwise AND of Numbers Range problem"""

    def setup_method(self):
        """Setup test fixtures"""
        self.solution = Solution()

    def test_example_1(self):
        """Test case from example 1"""
        assert self.solution.rangeBitwiseAnd(5, 7) == 4

    def test_example_2(self):
        """Test case from example 2"""
        assert self.solution.rangeBitwiseAnd(0, 0) == 0

    def test_example_3(self):
        """Test case from example 3"""
        assert self.solution.rangeBitwiseAnd(1, 2147483647) == 0
