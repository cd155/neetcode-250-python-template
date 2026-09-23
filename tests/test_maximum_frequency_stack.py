"""
Tests for LeetCode 895: Maximum Frequency Stack
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

# Import using importlib to avoid conflicts with built-in modules
import importlib.util
spec = importlib.util.spec_from_file_location("maximum_frequency_stack", src_path / "stack" / "maximum_frequency_stack.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
FreqStack = module.FreqStack


class TestMaximumFrequencyStack:
    """Test cases for Maximum Frequency Stack problem"""

    def test_example_1(self):
        """Test case from example 1"""
        freqStack = FreqStack()
        freqStack.push(5)
        freqStack.push(7)
        freqStack.push(5)
        freqStack.push(7)
        freqStack.push(4)
        freqStack.push(5)
        assert freqStack.pop() == 5
        assert freqStack.pop() == 7
        assert freqStack.pop() == 5
        assert freqStack.pop() == 4
