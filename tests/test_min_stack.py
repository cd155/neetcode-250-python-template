"""
Tests for LeetCode 155: Min Stack
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

# Import using importlib to avoid conflicts with built-in modules
import importlib.util
spec = importlib.util.spec_from_file_location("min_stack", src_path / "stack" / "min_stack.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
MinStack = module.MinStack


class TestMinStack:
    """Test cases for Min Stack problem"""

    def test_example_1(self):
        """Test case from example 1"""
        minStack = MinStack()
        minStack.push(-2)
        minStack.push(0)
        minStack.push(-3)
        assert minStack.getMin() == -3
        minStack.pop()
        assert minStack.top() == 0
        assert minStack.getMin() == -2
