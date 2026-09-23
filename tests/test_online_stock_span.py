"""
Tests for LeetCode 901: Online Stock Span
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

# Import using importlib to avoid conflicts with built-in modules
import importlib.util
spec = importlib.util.spec_from_file_location("online_stock_span", src_path / "stack" / "online_stock_span.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
StockSpanner = module.StockSpanner


class TestOnlineStockSpan:
    """Test cases for Online Stock Span problem"""

    def test_example_1(self):
        """Test case from example 1"""
        stockSpanner = StockSpanner()
        assert stockSpanner.next(100) == 1
        assert stockSpanner.next(80) == 1
        assert stockSpanner.next(60) == 1
        assert stockSpanner.next(70) == 2
        assert stockSpanner.next(60) == 1
        assert stockSpanner.next(75) == 4
        assert stockSpanner.next(85) == 6
