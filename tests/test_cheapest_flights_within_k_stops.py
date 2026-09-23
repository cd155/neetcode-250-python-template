"""
Tests for LeetCode 787: Cheapest Flights Within K Stops
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

# Import using importlib to avoid conflicts with built-in modules
import importlib.util
spec = importlib.util.spec_from_file_location("cheapest_flights_within_k_stops", src_path / "advanced_graphs" / "cheapest_flights_within_k_stops.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
Solution = module.Solution


class TestCheapestFlightsWithinKStops:
    """Test cases for Cheapest Flights Within K Stops problem"""

    def setup_method(self):
        """Setup test fixtures"""
        self.solution = Solution()

    def test_example_1(self):
        """Test case from example 1"""
        n = 4
        flights = [[0, 1, 100], [1, 2, 100], [2, 0, 100], [1, 3, 600], [2, 3, 200]]
        src = 0
        dst = 3
        k = 1
        result = self.solution.findCheapestPrice(n, flights, src, dst, k)
        assert result == 700

    def test_example_2(self):
        """Test case from example 2"""
        n = 3
        flights = [[0, 1, 100], [1, 2, 100], [0, 2, 500]]
        src = 0
        dst = 2
        k = 1
        result = self.solution.findCheapestPrice(n, flights, src, dst, k)
        assert result == 200

    def test_example_3(self):
        """Test case from example 3"""
        n = 3
        flights = [[0, 1, 100], [1, 2, 100], [0, 2, 500]]
        src = 0
        dst = 2
        k = 0
        result = self.solution.findCheapestPrice(n, flights, src, dst, k)
        assert result == 500
