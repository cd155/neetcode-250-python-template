"""
Tests for LeetCode 1094: Car Pooling
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

# Import using importlib to avoid conflicts with built-in modules
import importlib.util
spec = importlib.util.spec_from_file_location("car_pooling", src_path / "heap_priority_queue" / "car_pooling.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
Solution = module.Solution


class TestCarPooling:
    """Test cases for Car Pooling problem"""

    def setup_method(self):
        """Setup test fixtures"""
        self.solution = Solution()

    def test_example_1(self):
        """Test case from example 1"""
        assert self.solution.carPooling([[2, 1, 5], [3, 3, 7]], 4) is False

    def test_example_2(self):
        """Test case from example 2"""
        assert self.solution.carPooling([[2, 1, 5], [3, 3, 7]], 5) is True
