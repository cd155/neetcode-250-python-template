"""
Tests for LeetCode 22: Generate Parentheses
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

# Import using importlib to avoid conflicts with built-in modules
import importlib.util
spec = importlib.util.spec_from_file_location("generate_parentheses", src_path / "stack" / "generate_parentheses.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
Solution = module.Solution


class TestGenerateParentheses:
    """Test cases for Generate Parentheses problem"""

    def setup_method(self):
        """Setup test fixtures"""
        self.solution = Solution()

    def test_example_1(self):
        """Test case from example 1"""
        result = self.solution.generateParenthesis(3)
        assert sorted(result) == ["((()))", "(()())", "(())()", "()(())", "()()()"]

    def test_example_2(self):
        """Test case from example 2"""
        assert sorted(self.solution.generateParenthesis(1)) == ["()"]
