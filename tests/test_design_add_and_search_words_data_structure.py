"""
Tests for LeetCode 211: Design Add and Search Words Data Structure
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

# Import using importlib to avoid conflicts with built-in modules
import importlib.util
spec = importlib.util.spec_from_file_location("design_add_and_search_words_data_structure", src_path / "tries" / "design_add_and_search_words_data_structure.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
WordDictionary = module.WordDictionary


class TestDesignAddAndSearchWordsDataStructure:
    """Test cases for Design Add and Search Words Data Structure problem"""

    def test_example_1(self):
        """Test case from example 1"""
        wordDictionary = WordDictionary()
        wordDictionary.addWord("bad")
        wordDictionary.addWord("dad")
        wordDictionary.addWord("mad")
        assert wordDictionary.search("pad") is False
        assert wordDictionary.search("bad") is True
        assert wordDictionary.search(".ad") is True
        assert wordDictionary.search("b..") is True
