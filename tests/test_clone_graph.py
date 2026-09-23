"""
Tests for LeetCode 133: Clone Graph
"""

import pytest
import sys
from collections import deque
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

# Import using importlib to avoid conflicts with built-in modules
import importlib.util
spec = importlib.util.spec_from_file_location("clone_graph", src_path / "graphs" / "clone_graph.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
Solution = module.Solution
Node = module.Node


def build_graph(adj_list):
    """Build a graph from its adjacency list (node i + 1 has neighbors adj_list[i]) and return node 1."""
    nodes = [Node(i + 1) for i in range(len(adj_list))]
    for node, neighbors in zip(nodes, adj_list):
        node.neighbors = [nodes[j - 1] for j in neighbors]
    return nodes[0] if nodes else None


def graph_nodes(node):
    """Return every node reachable from node, sorted by value."""
    if node is None:
        return []
    seen = {id(node): node}
    queue = deque([node])
    while queue:
        for neighbor in queue.popleft().neighbors:
            if id(neighbor) not in seen:
                seen[id(neighbor)] = neighbor
                queue.append(neighbor)
    return sorted(seen.values(), key=lambda n: n.val)


def graph_to_adj_list(node):
    """Convert the graph reachable from node to its adjacency list."""
    return [[neighbor.val for neighbor in n.neighbors] for n in graph_nodes(node)]


def shares_nodes(node1, node2):
    """Check whether two graphs share any node object."""
    ids = {id(n) for n in graph_nodes(node1)}
    return any(id(n) in ids for n in graph_nodes(node2))


class TestCloneGraph:
    """Test cases for Clone Graph problem"""

    def setup_method(self):
        """Setup test fixtures"""
        self.solution = Solution()

    def test_example_1(self):
        """Test case from example 1"""
        node = build_graph([[2, 4], [1, 3], [2, 4], [1, 3]])
        cloned = self.solution.cloneGraph(node)
        assert graph_to_adj_list(cloned) == [[2, 4], [1, 3], [2, 4], [1, 3]]
        assert not shares_nodes(node, cloned)

    def test_example_2(self):
        """Test case from example 2"""
        node = build_graph([[]])
        cloned = self.solution.cloneGraph(node)
        assert graph_to_adj_list(cloned) == [[]]
        assert not shares_nodes(node, cloned)

    def test_example_3(self):
        """Test case from example 3"""
        assert self.solution.cloneGraph(None) is None
