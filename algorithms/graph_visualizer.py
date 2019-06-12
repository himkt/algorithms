"""Graph visualizer."""
import graphviz


class GraphVisualizer:
    """Visualize tree using depth first search."""

    def __init__(self, name):
        """Initializer."""
        self.name = name
        self.nodes = []
        self.edges = []

    def __call__(self, root_node):
        """Create graphviz format graph."""
        self._dfs(root_node)

        g = graphviz.Digraph(filename=self.name + '.pdf')
        g.attr("node", shape="circle")

        for edge in self.edges:
            g.edge(edge[0], edge[1])

        g.render(self.name, view=True)

    def _dfs(self, node):
        if node.right:
            self.nodes.append(f'{node}')
            self.edges.append([str(node), str(node.right)])
            self._dfs(node.right)

        if node.left:
            self.nodes.append(f'{node}')
            self.edges.append([str(node), str(node.left)])
            self._dfs(node.left)

        self.nodes.append(f'{node}')
