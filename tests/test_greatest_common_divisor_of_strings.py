"""
Tests for LeetCode 1071: Greatest Common Divisor of Strings
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

# Import using importlib to avoid conflicts with built-in modules
import importlib.util
spec = importlib.util.spec_from_file_location("greatest_common_divisor_of_strings", src_path / "math_and_geometry" / "greatest_common_divisor_of_strings.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
Solution = module.Solution


class TestGreatestCommonDivisorOfStrings:
    """Test cases for Greatest Common Divisor of Strings problem"""

    def setup_method(self):
        """Setup test fixtures"""
        self.solution = Solution()

    def test_example_1(self):
        """Test case from example 1"""
        assert self.solution.gcdOfStrings("ABCABC", "ABC") == "ABC"

    def test_example_2(self):
        """Test case from example 2"""
        assert self.solution.gcdOfStrings("ABABAB", "ABAB") == "AB"

    def test_example_3(self):
        """Test case from example 3"""
        assert self.solution.gcdOfStrings("LEET", "CODE") == ""

    def test_example_4(self):
        """Test case from example 4"""
        assert self.solution.gcdOfStrings("AAAAAB", "AAA") == ""
