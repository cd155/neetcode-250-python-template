"""
Tests for LeetCode 269: Alien Dictionary
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

# Import using importlib to avoid conflicts with built-in modules
import importlib.util
spec = importlib.util.spec_from_file_location("alien_dictionary", src_path / "advanced_graphs" / "alien_dictionary.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
Solution = module.Solution


def is_valid_alien_order(words, order):
    """Check that order lists every letter once and sorts words lexicographically."""
    if not isinstance(order, str) or sorted(order) != sorted(set("".join(words))):
        return False
    rank = {letter: i for i, letter in enumerate(order)}
    keys = [[rank[letter] for letter in word] for word in words]
    return keys == sorted(keys)


class TestAlienDictionary:
    """Test cases for Alien Dictionary problem"""

    def setup_method(self):
        """Setup test fixtures"""
        self.solution = Solution()

    def test_example_1(self):
        """Test case from example 1 (any valid order is accepted)"""
        words = ["wrt", "wrf", "er", "ett", "rftt"]
        assert is_valid_alien_order(words, self.solution.alienOrder(words))

    def test_example_2(self):
        """Test case from example 2"""
        assert self.solution.alienOrder(["z", "x"]) == "zx"

    def test_example_3(self):
        """Test case from example 3"""
        assert self.solution.alienOrder(["z", "x", "z"]) == ""
