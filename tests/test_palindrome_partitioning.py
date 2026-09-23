"""
Tests for LeetCode 131: Palindrome Partitioning
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

# Import using importlib to avoid conflicts with built-in modules
import importlib.util
spec = importlib.util.spec_from_file_location("palindrome_partitioning", src_path / "backtracking" / "palindrome_partitioning.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
Solution = module.Solution


class TestPalindromePartitioning:
    """Test cases for Palindrome Partitioning problem"""

    def setup_method(self):
        """Setup test fixtures"""
        self.solution = Solution()

    def test_example_1(self):
        """Test case from example 1"""
        assert sorted(self.solution.partition("aab")) == [["a", "a", "b"], ["aa", "b"]]

    def test_example_2(self):
        """Test case from example 2"""
        assert sorted(self.solution.partition("a")) == [["a"]]
