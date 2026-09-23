"""
Tests for LeetCode 867: Transpose Matrix
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

# Import using importlib to avoid conflicts with built-in modules
import importlib.util
spec = importlib.util.spec_from_file_location("transpose_matrix", src_path / "math_and_geometry" / "transpose_matrix.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
Solution = module.Solution


class TestTransposeMatrix:
    """Test cases for Transpose Matrix problem"""

    def setup_method(self):
        """Setup test fixtures"""
        self.solution = Solution()

    def test_example_1(self):
        """Test case from example 1"""
        result = self.solution.transpose([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        assert [list(row) for row in result] == [[1, 4, 7], [2, 5, 8], [3, 6, 9]]

    def test_example_2(self):
        """Test case from example 2"""
        result = self.solution.transpose([[1, 2, 3], [4, 5, 6]])
        assert [list(row) for row in result] == [[1, 4], [2, 5], [3, 6]]
