"""Huffman coding."""

from algorithms.graph_visualizer import GraphVisualizer
from algorithms.huffman import HuffmanCodeBuilder
from algorithms.huffman import SymbolCodeNode


if __name__ == '__main__':
    words = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k']
    freqs = [100,  70,  20,  25,  40,  10,  15,   2,   1,   1,   1]

    # construct huffman tree
    nodes = [SymbolCodeNode(w, f) for w, f in zip(words, freqs)]
    builder = HuffmanCodeBuilder()
    root_node = builder.construct(nodes)

    # visualize huffman tree
    graph_visualizer = GraphVisualizer(name='huffman')
    graph_visualizer(root_node)
