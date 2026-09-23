"""
Tests for LeetCode 97: Interleaving String
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

# Import using importlib to avoid conflicts with built-in modules
import importlib.util
spec = importlib.util.spec_from_file_location("interleaving_string", src_path / "dp_2d" / "interleaving_string.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
Solution = module.Solution


class TestInterleavingString:
    """Test cases for Interleaving String problem"""

    def setup_method(self):
        """Setup test fixtures"""
        self.solution = Solution()

    def test_example_1(self):
        """Test case from example 1"""
        assert self.solution.isInterleave("aabcc", "dbbca", "aadbbcbcac") is True

    def test_example_2(self):
        """Test case from example 2"""
        assert self.solution.isInterleave("aabcc", "dbbca", "aadbbbaccc") is False

    def test_example_3(self):
        """Test case from example 3"""
        assert self.solution.isInterleave("", "", "") is True
