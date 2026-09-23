"""
Tests for LeetCode 225: Implement Stack using Queues
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

# Import using importlib to avoid conflicts with built-in modules
import importlib.util
spec = importlib.util.spec_from_file_location("implement_stack_using_queues", src_path / "stack" / "implement_stack_using_queues.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
MyStack = module.MyStack


class TestImplementStackUsingQueues:
    """Test cases for Implement Stack using Queues problem"""

    def test_example_1(self):
        """Test case from example 1"""
        myStack = MyStack()
        myStack.push(1)
        myStack.push(2)
        assert myStack.top() == 2
        assert myStack.pop() == 2
        assert myStack.empty() is False
