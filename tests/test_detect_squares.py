"""
Tests for LeetCode 2013: Detect Squares
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

# Import using importlib to avoid conflicts with built-in modules
import importlib.util
spec = importlib.util.spec_from_file_location("detect_squares", src_path / "math_and_geometry" / "detect_squares.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
DetectSquares = module.DetectSquares


class TestDetectSquares:
    """Test cases for Detect Squares problem"""

    def test_example_1(self):
        """Test case from example 1"""
        detectSquares = DetectSquares()
        detectSquares.add([3, 10])
        detectSquares.add([11, 2])
        detectSquares.add([3, 2])
        assert detectSquares.count([11, 10]) == 1
        assert detectSquares.count([14, 8]) == 0
        detectSquares.add([11, 2])
        assert detectSquares.count([11, 10]) == 2
