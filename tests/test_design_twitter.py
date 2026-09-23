"""
Tests for LeetCode 355: Design Twitter
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

# Import using importlib to avoid conflicts with built-in modules
import importlib.util
spec = importlib.util.spec_from_file_location("design_twitter", src_path / "heap_priority_queue" / "design_twitter.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
Twitter = module.Twitter


class TestDesignTwitter:
    """Test cases for Design Twitter problem"""

    def test_example_1(self):
        """Test case from example 1"""
        twitter = Twitter()
        twitter.postTweet(1, 5)
        assert twitter.getNewsFeed(1) == [5]
        twitter.follow(1, 2)
        twitter.postTweet(2, 6)
        assert twitter.getNewsFeed(1) == [6, 5]
        twitter.unfollow(1, 2)
        assert twitter.getNewsFeed(1) == [5]
