"""
Tests for LeetCode 52: N-Queens II
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

# Import using importlib to avoid conflicts with built-in modules
import importlib.util
spec = importlib.util.spec_from_file_location("n_queens_ii", src_path / "backtracking" / "n_queens_ii.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
Solution = module.Solution


class TestNQueensII:
    """Test cases for N-Queens II problem"""

    def setup_method(self):
        """Setup test fixtures"""
        self.solution = Solution()

    def test_example_1(self):
        """Test case from example 1"""
        assert self.solution.totalNQueens(4) == 2

    def test_example_2(self):
        """Test case from example 2"""
        assert self.solution.totalNQueens(1) == 1
