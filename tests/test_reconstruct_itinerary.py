"""
Tests for LeetCode 332: Reconstruct Itinerary
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

# Import using importlib to avoid conflicts with built-in modules
import importlib.util
spec = importlib.util.spec_from_file_location("reconstruct_itinerary", src_path / "advanced_graphs" / "reconstruct_itinerary.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
Solution = module.Solution


class TestReconstructItinerary:
    """Test cases for Reconstruct Itinerary problem"""

    def setup_method(self):
        """Setup test fixtures"""
        self.solution = Solution()

    def test_example_1(self):
        """Test case from example 1"""
        tickets = [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
        result = self.solution.findItinerary(tickets)
        assert result == ["JFK", "MUC", "LHR", "SFO", "SJC"]

    def test_example_2(self):
        """Test case from example 2"""
        tickets = [["JFK", "SFO"], ["JFK", "ATL"], ["SFO", "ATL"], ["ATL", "JFK"], ["ATL", "SFO"]]
        result = self.solution.findItinerary(tickets)
        assert result == ["JFK", "ATL", "JFK", "SFO", "ATL", "SFO"]
