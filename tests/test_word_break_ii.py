"""
Tests for LeetCode 140: Word Break II
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

# Import using importlib to avoid conflicts with built-in modules
import importlib.util
spec = importlib.util.spec_from_file_location("word_break_ii", src_path / "backtracking" / "word_break_ii.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
Solution = module.Solution


class TestWordBreakII:
    """Test cases for Word Break II problem"""

    def setup_method(self):
        """Setup test fixtures"""
        self.solution = Solution()

    def test_example_1(self):
        """Test case from example 1"""
        result = self.solution.wordBreak("catsanddog", ["cat", "cats", "and", "sand", "dog"])
        assert sorted(result) == ["cat sand dog", "cats and dog"]

    def test_example_2(self):
        """Test case from example 2"""
        s = "pineapplepenapple"
        wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
        result = self.solution.wordBreak(s, wordDict)
        expected = ["pine apple pen apple", "pine applepen apple", "pineapple pen apple"]
        assert sorted(result) == expected

    def test_example_3(self):
        """Test case from example 3"""
        result = self.solution.wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"])
        assert sorted(result) == []
