"""
Tests for LeetCode 684: Redundant Connection
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

# Import using importlib to avoid conflicts with built-in modules
import importlib.util
spec = importlib.util.spec_from_file_location("redundant_connection", src_path / "graphs" / "redundant_connection.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
Solution = module.Solution


class TestRedundantConnection:
    """Test cases for Redundant Connection problem"""

    def setup_method(self):
        """Setup test fixtures"""
        self.solution = Solution()

    def test_example_1(self):
        """Test case from example 1"""
        assert self.solution.findRedundantConnection([[1, 2], [1, 3], [2, 3]]) == [2, 3]

    def test_example_2(self):
        """Test case from example 2"""
        result = self.solution.findRedundantConnection([[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]])
        assert result == [1, 4]
