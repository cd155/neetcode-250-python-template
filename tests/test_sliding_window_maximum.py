"""
Tests for LeetCode 239: Sliding Window Maximum
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

# Import using importlib to avoid conflicts with built-in modules
import importlib.util
spec = importlib.util.spec_from_file_location("sliding_window_maximum", src_path / "sliding_window" / "sliding_window_maximum.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
Solution = module.Solution


class TestSlidingWindowMaximum:
    """Test cases for Sliding Window Maximum problem"""

    def setup_method(self):
        """Setup test fixtures"""
        self.solution = Solution()

    def test_example_1(self):
        """Test case from example 1"""
        assert self.solution.maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3) == [3, 3, 5, 5, 6, 7]

    def test_example_2(self):
        """Test case from example 2"""
        assert self.solution.maxSlidingWindow([1], 1) == [1]
