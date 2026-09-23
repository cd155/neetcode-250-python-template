"""
Tests for LeetCode 309: Best Time to Buy and Sell Stock with Cooldown
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

# Import using importlib to avoid conflicts with built-in modules
import importlib.util
spec = importlib.util.spec_from_file_location("best_time_to_buy_and_sell_stock_with_cooldown", src_path / "dp_2d" / "best_time_to_buy_and_sell_stock_with_cooldown.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
Solution = module.Solution


class TestBestTimeToBuyAndSellStockWithCooldown:
    """Test cases for Best Time to Buy and Sell Stock with Cooldown problem"""

    def setup_method(self):
        """Setup test fixtures"""
        self.solution = Solution()

    def test_example_1(self):
        """Test case from example 1"""
        assert self.solution.maxProfit([1, 2, 3, 0, 2]) == 3

    def test_example_2(self):
        """Test case from example 2"""
        assert self.solution.maxProfit([1]) == 0
