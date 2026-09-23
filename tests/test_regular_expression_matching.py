"""
Tests for LeetCode 10: Regular Expression Matching
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

# Import using importlib to avoid conflicts with built-in modules
import importlib.util
spec = importlib.util.spec_from_file_location("regular_expression_matching", src_path / "dp_2d" / "regular_expression_matching.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
Solution = module.Solution


class TestRegularExpressionMatching:
    """Test cases for Regular Expression Matching problem"""

    def setup_method(self):
        """Setup test fixtures"""
        self.solution = Solution()

    def test_example_1(self):
        """Test case from example 1"""
        assert self.solution.isMatch("aa", "a") is False

    def test_example_2(self):
        """Test case from example 2"""
        assert self.solution.isMatch("aa", "a*") is True

    def test_example_3(self):
        """Test case from example 3"""
        assert self.solution.isMatch("ab", ".*") is True
