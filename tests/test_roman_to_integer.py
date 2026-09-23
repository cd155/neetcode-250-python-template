"""
Tests for LeetCode 13: Roman to Integer
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

# Import using importlib to avoid conflicts with built-in modules
import importlib.util
spec = importlib.util.spec_from_file_location("roman_to_integer", src_path / "math_and_geometry" / "roman_to_integer.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
Solution = module.Solution


class TestRomanToInteger:
    """Test cases for Roman to Integer problem"""

    def setup_method(self):
        """Setup test fixtures"""
        self.solution = Solution()

    def test_example_1(self):
        """Test case from example 1"""
        assert self.solution.romanToInt("III") == 3

    def test_example_2(self):
        """Test case from example 2"""
        assert self.solution.romanToInt("LVIII") == 58

    def test_example_3(self):
        """Test case from example 3"""
        assert self.solution.romanToInt("MCMXCIV") == 1994
