"""
Tests for LeetCode 2392: Build a Matrix With Conditions
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

# Import using importlib to avoid conflicts with built-in modules
import importlib.util
spec = importlib.util.spec_from_file_location("build_a_matrix_with_conditions", src_path / "advanced_graphs" / "build_a_matrix_with_conditions.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
Solution = module.Solution


def is_valid_matrix(k, row_conditions, col_conditions, matrix):
    """Check that matrix is k x k, holds 1..k once each (0 elsewhere) and meets every condition."""
    if not isinstance(matrix, list) or len(matrix) != k or any(len(row) != k for row in matrix):
        return False
    cells = {value: (r, c) for r, row in enumerate(matrix) for c, value in enumerate(row) if value}
    if sorted(cells) != list(range(1, k + 1)) or sum(1 for row in matrix for v in row if v) != k:
        return False
    rows_ok = all(cells[above][0] < cells[below][0] for above, below in row_conditions)
    cols_ok = all(cells[left][1] < cells[right][1] for left, right in col_conditions)
    return rows_ok and cols_ok


class TestBuildAMatrixWithConditions:
    """Test cases for Build a Matrix With Conditions problem"""

    def setup_method(self):
        """Setup test fixtures"""
        self.solution = Solution()

    def test_example_1(self):
        """Test case from example 1 (any valid matrix is accepted)"""
        row_conditions = [[1, 2], [3, 2]]
        col_conditions = [[2, 1], [3, 2]]
        result = self.solution.buildMatrix(3, row_conditions, col_conditions)
        assert is_valid_matrix(3, row_conditions, col_conditions, result)

    def test_example_2(self):
        """Test case from example 2"""
        assert self.solution.buildMatrix(3, [[1, 2], [2, 3], [3, 1], [2, 3]], [[2, 1]]) == []
