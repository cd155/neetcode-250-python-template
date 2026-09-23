"""
Tests for LeetCode 1631: Path With Minimum Effort
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

# Import using importlib to avoid conflicts with built-in modules
import importlib.util
spec = importlib.util.spec_from_file_location("path_with_minimum_effort", src_path / "advanced_graphs" / "path_with_minimum_effort.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
Solution = module.Solution


class TestPathWithMinimumEffort:
    """Test cases for Path With Minimum Effort problem"""

    def setup_method(self):
        """Setup test fixtures"""
        self.solution = Solution()

    def test_example_1(self):
        """Test case from example 1"""
        assert self.solution.minimumEffortPath([[1, 2, 2], [3, 8, 2], [5, 3, 5]]) == 2

    def test_example_2(self):
        """Test case from example 2"""
        assert self.solution.minimumEffortPath([[1, 2, 3], [3, 8, 4], [5, 3, 5]]) == 1

    def test_example_3(self):
        """Test case from example 3"""
        heights = [
            [1, 2, 1, 1, 1],
            [1, 2, 1, 2, 1],
            [1, 2, 1, 2, 1],
            [1, 2, 1, 2, 1],
            [1, 1, 1, 2, 1],
        ]
        result = self.solution.minimumEffortPath(heights)
        assert result == 0
