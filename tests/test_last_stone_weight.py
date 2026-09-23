"""
Tests for LeetCode 1046: Last Stone Weight
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

# Import using importlib to avoid conflicts with built-in modules
import importlib.util
spec = importlib.util.spec_from_file_location("last_stone_weight", src_path / "heap_priority_queue" / "last_stone_weight.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
Solution = module.Solution


class TestLastStoneWeight:
    """Test cases for Last Stone Weight problem"""

    def setup_method(self):
        """Setup test fixtures"""
        self.solution = Solution()

    def test_example_1(self):
        """Test case from example 1"""
        assert self.solution.lastStoneWeight([2, 7, 4, 1, 8, 1]) == 1

    def test_example_2(self):
        """Test case from example 2"""
        assert self.solution.lastStoneWeight([1]) == 1
