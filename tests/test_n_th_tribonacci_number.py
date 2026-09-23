"""
Tests for LeetCode 1137: N-th Tribonacci Number
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

# Import using importlib to avoid conflicts with built-in modules
import importlib.util
spec = importlib.util.spec_from_file_location("n_th_tribonacci_number", src_path / "dp_1d" / "n_th_tribonacci_number.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
Solution = module.Solution


class TestNThTribonacciNumber:
    """Test cases for N-th Tribonacci Number problem"""

    def setup_method(self):
        """Setup test fixtures"""
        self.solution = Solution()

    def test_example_1(self):
        """Test case from example 1"""
        assert self.solution.tribonacci(4) == 4

    def test_example_2(self):
        """Test case from example 2"""
        assert self.solution.tribonacci(25) == 1389537
