"""
Tests for LeetCode 50: Pow(x, n)
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

# Import using importlib to avoid conflicts with built-in modules
import importlib.util
spec = importlib.util.spec_from_file_location("powx_n", src_path / "math_and_geometry" / "powx_n.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
Solution = module.Solution


class TestPowxN:
    """Test cases for Pow(x, n) problem"""

    def setup_method(self):
        """Setup test fixtures"""
        self.solution = Solution()

    def test_example_1(self):
        """Test case from example 1"""
        assert self.solution.myPow(2.0, 10) == pytest.approx(1024.0)

    def test_example_2(self):
        """Test case from example 2"""
        assert self.solution.myPow(2.1, 3) == pytest.approx(9.261)

    def test_example_3(self):
        """Test case from example 3"""
        assert self.solution.myPow(2.0, -2) == pytest.approx(0.25)
