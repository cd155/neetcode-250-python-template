"""
Tests for LeetCode 1405: Longest Happy String
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

# Import using importlib to avoid conflicts with built-in modules
import importlib.util
spec = importlib.util.spec_from_file_location("longest_happy_string", src_path / "heap_priority_queue" / "longest_happy_string.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
Solution = module.Solution


def is_happy(result, a, b, c):
    """Check that result is a happy string using at most a 'a', b 'b' and c 'c' letters."""
    if not isinstance(result, str) or set(result) - set("abc"):
        return False
    if "aaa" in result or "bbb" in result or "ccc" in result:
        return False
    return result.count("a") <= a and result.count("b") <= b and result.count("c") <= c


class TestLongestHappyString:
    """Test cases for Longest Happy String problem"""

    def setup_method(self):
        """Setup test fixtures"""
        self.solution = Solution()

    def test_example_1(self):
        """Test case from example 1 (any longest happy string is accepted)"""
        result = self.solution.longestDiverseString(1, 1, 7)
        assert is_happy(result, 1, 1, 7)
        assert len(result) == len("ccaccbcc")

    def test_example_2(self):
        """Test case from example 2 (any longest happy string is accepted)"""
        result = self.solution.longestDiverseString(7, 1, 0)
        assert is_happy(result, 7, 1, 0)
        assert len(result) == len("aabaa")
