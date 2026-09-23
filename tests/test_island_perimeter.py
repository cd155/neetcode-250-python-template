"""
Tests for LeetCode 463: Island Perimeter
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

# Import using importlib to avoid conflicts with built-in modules
import importlib.util
spec = importlib.util.spec_from_file_location("island_perimeter", src_path / "graphs" / "island_perimeter.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
Solution = module.Solution


class TestIslandPerimeter:
    """Test cases for Island Perimeter problem"""

    def setup_method(self):
        """Setup test fixtures"""
        self.solution = Solution()

    def test_example_1(self):
        """Test case from example 1"""
        grid = [[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]]
        result = self.solution.islandPerimeter(grid)
        assert result == 16

    def test_example_2(self):
        """Test case from example 2"""
        assert self.solution.islandPerimeter([[1]]) == 4

    def test_example_3(self):
        """Test case from example 3"""
        assert self.solution.islandPerimeter([[1, 0]]) == 4
