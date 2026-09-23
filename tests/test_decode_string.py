"""
Tests for LeetCode 394: Decode String
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

# Import using importlib to avoid conflicts with built-in modules
import importlib.util
spec = importlib.util.spec_from_file_location("decode_string", src_path / "stack" / "decode_string.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
Solution = module.Solution


class TestDecodeString:
    """Test cases for Decode String problem"""

    def setup_method(self):
        """Setup test fixtures"""
        self.solution = Solution()

    def test_example_1(self):
        """Test case from example 1"""
        assert self.solution.decodeString("3[a]2[bc]") == "aaabcbc"

    def test_example_2(self):
        """Test case from example 2"""
        assert self.solution.decodeString("3[a2[c]]") == "accaccacc"

    def test_example_3(self):
        """Test case from example 3"""
        assert self.solution.decodeString("2[abc]3[cd]ef") == "abcabccdcdcdef"
