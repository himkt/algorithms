"""Test Huffman."""

from algorithms.huffman import SymbolCodeNode

import unittest


class TestHuffman(unittest.TestCase):
    """Test huffman tree class."""

    def test_huffman(self):
        """Test symbol."""
        node1 = SymbolCodeNode('word1', 10)
        node2 = SymbolCodeNode('word2', 20)
        self.assertTrue(node1 < node2)
