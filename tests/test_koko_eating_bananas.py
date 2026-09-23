"""
Tests for LeetCode 875: Koko Eating Bananas
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

# Import using importlib to avoid conflicts with built-in modules
import importlib.util
spec = importlib.util.spec_from_file_location("koko_eating_bananas", src_path / "binary_search" / "koko_eating_bananas.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
Solution = module.Solution


class TestKokoEatingBananas:
    """Test cases for Koko Eating Bananas problem"""

    def setup_method(self):
        """Setup test fixtures"""
        self.solution = Solution()

    def test_example_1(self):
        """Test case from example 1"""
        assert self.solution.minEatingSpeed([3, 6, 7, 11], 8) == 4

    def test_example_2(self):
        """Test case from example 2"""
        assert self.solution.minEatingSpeed([30, 11, 23, 4, 20], 5) == 30

    def test_example_3(self):
        """Test case from example 3"""
        assert self.solution.minEatingSpeed([30, 11, 23, 4, 20], 6) == 23
