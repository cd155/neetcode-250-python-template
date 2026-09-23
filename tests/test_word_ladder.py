"""
Tests for LeetCode 127: Word Ladder
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

# Import using importlib to avoid conflicts with built-in modules
import importlib.util
spec = importlib.util.spec_from_file_location("word_ladder", src_path / "graphs" / "word_ladder.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
Solution = module.Solution


class TestWordLadder:
    """Test cases for Word Ladder problem"""

    def setup_method(self):
        """Setup test fixtures"""
        self.solution = Solution()

    def test_example_1(self):
        """Test case from example 1"""
        beginWord = "hit"
        endWord = "cog"
        wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
        result = self.solution.ladderLength(beginWord, endWord, wordList)
        assert result == 5

    def test_example_2(self):
        """Test case from example 2"""
        assert self.solution.ladderLength("hit", "cog", ["hot", "dot", "dog", "lot", "log"]) == 0
