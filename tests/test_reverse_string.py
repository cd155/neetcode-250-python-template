"""
Tests for LeetCode 344: Reverse String
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

# Import using importlib to avoid conflicts with built-in modules
import importlib.util
spec = importlib.util.spec_from_file_location("reverse_string", src_path / "two_pointers" / "reverse_string.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
Solution = module.Solution


class TestReverseString:
    """Test cases for Reverse String problem"""

    def setup_method(self):
        """Setup test fixtures"""
        self.solution = Solution()

    def test_example_1(self):
        """Test case from example 1"""
        s = ["h", "e", "l", "l", "o"]
        self.solution.reverseString(s)
        assert s == ["o", "l", "l", "e", "h"]

    def test_example_2(self):
        """Test case from example 2"""
        s = ["H", "a", "n", "n", "a", "h"]
        self.solution.reverseString(s)
        assert s == ["h", "a", "n", "n", "a", "H"]
