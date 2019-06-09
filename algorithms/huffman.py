"""Huffman coding."""

from typing import List

import heapq


class SymbolCodeNode:
    """Node which is used in Huffman tree."""

    def __init__(self, w, f, left=None, right=None):
        """Node constructor."""
        self.word = w
        self.freq = f

        self.left = left
        self.right = right

    def __gt__(self, right):
        """Operator."""
        return self.freq > right.freq

    def __repr__(self):
        """Return str of symbol."""
        return f'Symbol_{self.word}'


class HuffmanCodeBuilder:
    """Construct Huffman tree."""

    def __init__(self):
        """Constructor."""
        self.num_nodes = None

    def construct(self, nodes: List[SymbolCodeNode]):
        """Construc a huffman tree from list of symbols.

        Arguments:
            nodes {List[SymbolCodeNode]} -- list of symbold
                each node has a surface and frequency
        """
        heapq.heapify(nodes)
        self.num_nodes = len(nodes)

        while len(nodes) >= 2:
            node_1 = heapq.heappop(nodes)
            node_2 = heapq.heappop(nodes)

            node_new = self._join_nodes(node_1, node_2)
            heapq.heappush(nodes, node_new)

        root_node = nodes[0]
        return root_node

    def _join_nodes(self, node_1, node_2):
        freq_sum = node_1.freq + node_2.freq
        self.num_nodes += 1

        node_id = self.num_nodes
        node = SymbolCodeNode(
            f'Internal_Symbol_{node_id}',
            freq_sum,
            left=node_1,
            right=node_2
        )

        return node
