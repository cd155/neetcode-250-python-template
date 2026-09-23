"""
Tests for LeetCode 67: Add Binary
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

# Import using importlib to avoid conflicts with built-in modules
import importlib.util
spec = importlib.util.spec_from_file_location("add_binary", src_path / "bit_manipulation" / "add_binary.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
Solution = module.Solution


class TestAddBinary:
    """Test cases for Add Binary problem"""

    def setup_method(self):
        """Setup test fixtures"""
        self.solution = Solution()

    def test_example_1(self):
        """Test case from example 1"""
        assert self.solution.addBinary("11", "1") == "100"

    def test_example_2(self):
        """Test case from example 2"""
        assert self.solution.addBinary("1010", "1011") == "10101"
