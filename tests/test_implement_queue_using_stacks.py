"""
Tests for LeetCode 232: Implement Queue using Stacks
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

# Import using importlib to avoid conflicts with built-in modules
import importlib.util
spec = importlib.util.spec_from_file_location("implement_queue_using_stacks", src_path / "stack" / "implement_queue_using_stacks.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
MyQueue = module.MyQueue


class TestImplementQueueUsingStacks:
    """Test cases for Implement Queue using Stacks problem"""

    def test_example_1(self):
        """Test case from example 1"""
        myQueue = MyQueue()
        myQueue.push(1)
        myQueue.push(2)
        assert myQueue.peek() == 1
        assert myQueue.pop() == 1
        assert myQueue.empty() is False
