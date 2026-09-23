"""
Tests for LeetCode 1768: Merge Strings Alternately
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

# Import using importlib to avoid conflicts with built-in modules
import importlib.util
spec = importlib.util.spec_from_file_location("merge_strings_alternately", src_path / "two_pointers" / "merge_strings_alternately.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
Solution = module.Solution


class TestMergeStringsAlternately:
    """Test cases for Merge Strings Alternately problem"""

    def setup_method(self):
        """Setup test fixtures"""
        self.solution = Solution()

    def test_example_1(self):
        """Test case from example 1"""
        assert self.solution.mergeAlternately("abc", "pqr") == "apbqcr"

    def test_example_2(self):
        """Test case from example 2"""
        assert self.solution.mergeAlternately("ab", "pqrs") == "apbqrs"

    def test_example_3(self):
        """Test case from example 3"""
        assert self.solution.mergeAlternately("abcd", "pq") == "apbqcd"
