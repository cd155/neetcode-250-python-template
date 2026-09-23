"""
Tests for LeetCode 304: Range Sum Query 2D - Immutable
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

# Import using importlib to avoid conflicts with built-in modules
import importlib.util
spec = importlib.util.spec_from_file_location("range_sum_query_2d_immutable", src_path / "arrays_and_hashing" / "range_sum_query_2d_immutable.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
NumMatrix = module.NumMatrix


class TestRangeSumQuery2DImmutable:
    """Test cases for Range Sum Query 2D - Immutable problem"""

    def test_example_1(self):
        """Test case from example 1"""
        matrix = [
            [3, 0, 1, 4, 2],
            [5, 6, 3, 2, 1],
            [1, 2, 0, 1, 5],
            [4, 1, 0, 1, 7],
            [1, 0, 3, 0, 5],
        ]
        numMatrix = NumMatrix(matrix)
        assert numMatrix.sumRegion(2, 1, 4, 3) == 8
        assert numMatrix.sumRegion(1, 1, 2, 2) == 11
        assert numMatrix.sumRegion(1, 2, 2, 4) == 12
