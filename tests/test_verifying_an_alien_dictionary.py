"""
Tests for LeetCode 953: Verifying an Alien Dictionary
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

# Import using importlib to avoid conflicts with built-in modules
import importlib.util
spec = importlib.util.spec_from_file_location("verifying_an_alien_dictionary", src_path / "graphs" / "verifying_an_alien_dictionary.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
Solution = module.Solution


class TestVerifyingAnAlienDictionary:
    """Test cases for Verifying an Alien Dictionary problem"""

    def setup_method(self):
        """Setup test fixtures"""
        self.solution = Solution()

    def test_example_1(self):
        """Test case from example 1"""
        result = self.solution.isAlienSorted(["hello", "leetcode"], "hlabcdefgijkmnopqrstuvwxyz")
        assert result is True

    def test_example_2(self):
        """Test case from example 2"""
        result = self.solution.isAlienSorted(["word", "world", "row"], "worldabcefghijkmnpqstuvxyz")
        assert result is False

    def test_example_3(self):
        """Test case from example 3"""
        assert self.solution.isAlienSorted(["apple", "app"], "abcdefghijklmnopqrstuvwxyz") is False
