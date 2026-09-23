"""
Tests for LeetCode 752: Open the Lock
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

# Import using importlib to avoid conflicts with built-in modules
import importlib.util
spec = importlib.util.spec_from_file_location("open_the_lock", src_path / "graphs" / "open_the_lock.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
Solution = module.Solution


class TestOpenTheLock:
    """Test cases for Open the Lock problem"""

    def setup_method(self):
        """Setup test fixtures"""
        self.solution = Solution()

    def test_example_1(self):
        """Test case from example 1"""
        assert self.solution.openLock(["0201", "0101", "0102", "1212", "2002"], "0202") == 6

    def test_example_2(self):
        """Test case from example 2"""
        assert self.solution.openLock(["8888"], "0009") == 1

    def test_example_3(self):
        """Test case from example 3"""
        deadends = ["8887", "8889", "8878", "8898", "8788", "8988", "7888", "9888"]
        target = "8888"
        result = self.solution.openLock(deadends, target)
        assert result == -1
