"""
Tests for LeetCode 17: Letter Combinations of a Phone Number
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

# Import using importlib to avoid conflicts with built-in modules
import importlib.util
spec = importlib.util.spec_from_file_location("letter_combinations_of_a_phone_number", src_path / "backtracking" / "letter_combinations_of_a_phone_number.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
Solution = module.Solution


class TestLetterCombinationsOfAPhoneNumber:
    """Test cases for Letter Combinations of a Phone Number problem"""

    def setup_method(self):
        """Setup test fixtures"""
        self.solution = Solution()

    def test_example_1(self):
        """Test case from example 1"""
        result = self.solution.letterCombinations("23")
        assert sorted(result) == ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]

    def test_example_2(self):
        """Test case from example 2"""
        assert sorted(self.solution.letterCombinations("2")) == ["a", "b", "c"]
