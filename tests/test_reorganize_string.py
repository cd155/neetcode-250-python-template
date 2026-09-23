"""
Tests for LeetCode 767: Reorganize String
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

# Import using importlib to avoid conflicts with built-in modules
import importlib.util
spec = importlib.util.spec_from_file_location("reorganize_string", src_path / "heap_priority_queue" / "reorganize_string.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
Solution = module.Solution


def is_valid_rearrangement(s, result):
    """Check that result uses the letters of s and has no two equal adjacent characters."""
    if not isinstance(result, str) or sorted(result) != sorted(s):
        return False
    return all(a != b for a, b in zip(result, result[1:]))


class TestReorganizeString:
    """Test cases for Reorganize String problem"""

    def setup_method(self):
        """Setup test fixtures"""
        self.solution = Solution()

    def test_example_1(self):
        """Test case from example 1 (any valid rearrangement is accepted)"""
        result = self.solution.reorganizeString("aab")
        assert is_valid_rearrangement("aab", result)

    def test_example_2(self):
        """Test case from example 2"""
        assert self.solution.reorganizeString("aaab") == ""
