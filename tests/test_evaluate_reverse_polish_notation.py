"""
Tests for LeetCode 150: Evaluate Reverse Polish Notation
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

# Import using importlib to avoid conflicts with built-in modules
import importlib.util
spec = importlib.util.spec_from_file_location("evaluate_reverse_polish_notation", src_path / "stack" / "evaluate_reverse_polish_notation.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
Solution = module.Solution


class TestEvaluateReversePolishNotation:
    """Test cases for Evaluate Reverse Polish Notation problem"""

    def setup_method(self):
        """Setup test fixtures"""
        self.solution = Solution()

    def test_example_1(self):
        """Test case from example 1"""
        assert self.solution.evalRPN(["2", "1", "+", "3", "*"]) == 9

    def test_example_2(self):
        """Test case from example 2"""
        assert self.solution.evalRPN(["4", "13", "5", "/", "+"]) == 6

    def test_example_3(self):
        """Test case from example 3"""
        tokens = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
        result = self.solution.evalRPN(tokens)
        assert result == 22
