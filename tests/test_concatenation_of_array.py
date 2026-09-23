"""
Tests for LeetCode 1929: Concatenation of Array
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

# Import using importlib to avoid conflicts with built-in modules
import importlib.util
spec = importlib.util.spec_from_file_location("concatenation_of_array", src_path / "arrays_and_hashing" / "concatenation_of_array.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
Solution = module.Solution


class TestConcatenationOfArray:
    """Test cases for Concatenation of Array problem"""

    def setup_method(self):
        """Setup test fixtures"""
        self.solution = Solution()

    def test_example_1(self):
        """Test case from example 1"""
        assert self.solution.getConcatenation([1, 2, 1]) == [1, 2, 1, 1, 2, 1]

    def test_example_2(self):
        """Test case from example 2"""
        assert self.solution.getConcatenation([1, 3, 2, 1]) == [1, 3, 2, 1, 1, 3, 2, 1]
