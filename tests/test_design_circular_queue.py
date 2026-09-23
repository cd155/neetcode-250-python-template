"""
Tests for LeetCode 622: Design Circular Queue
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

# Import using importlib to avoid conflicts with built-in modules
import importlib.util
spec = importlib.util.spec_from_file_location("design_circular_queue", src_path / "linked_list" / "design_circular_queue.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
MyCircularQueue = module.MyCircularQueue


class TestDesignCircularQueue:
    """Test cases for Design Circular Queue problem"""

    def test_example_1(self):
        """Test case from example 1"""
        myCircularQueue = MyCircularQueue(3)
        assert myCircularQueue.enQueue(1) is True
        assert myCircularQueue.enQueue(2) is True
        assert myCircularQueue.enQueue(3) is True
        assert myCircularQueue.enQueue(4) is False
        assert myCircularQueue.Rear() == 3
        assert myCircularQueue.isFull() is True
        assert myCircularQueue.deQueue() is True
        assert myCircularQueue.enQueue(4) is True
        assert myCircularQueue.Rear() == 4
