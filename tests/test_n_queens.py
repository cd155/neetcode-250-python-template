"""
Tests for LeetCode 51: N-Queens
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

# Import using importlib to avoid conflicts with built-in modules
import importlib.util
spec = importlib.util.spec_from_file_location("n_queens", src_path / "backtracking" / "n_queens.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
Solution = module.Solution


class TestNQueens:
    """Test cases for N-Queens problem"""

    def setup_method(self):
        """Setup test fixtures"""
        self.solution = Solution()

    def test_example_1(self):
        """Test case from example 1"""
        result = self.solution.solveNQueens(4)
        expected = [["..Q.", "Q...", "...Q", ".Q.."], [".Q..", "...Q", "Q...", "..Q."]]
        assert sorted(result) == expected

    def test_example_2(self):
        """Test case from example 2"""
        assert sorted(self.solution.solveNQueens(1)) == [["Q"]]
