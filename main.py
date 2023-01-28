import matplotlib.pylab as plt
import networkx as nx
import random

def td(graph, node):
    """
    td - topological descendants

    Return a topologically-ordered list of the descendants of *node* of *graph*.
    """
    return list(nx.topological_sort(graph.subgraph(nx.descendants(graph, node))))

adj = [
    (1, 7),
    (2, 7),
    (1, 8),
    (2, 8),
    (3, 8),
    (3, 9),
    (4, 9),
    (5, 10),
    (6, 10),
    (5, 11),
    (6, 11),
    (7, 12),
    (8, 12),
    (9, 13),
    (5, 13),
]
random.shuffle(adj)

G = nx.DiGraph()
G.add_edges_from(adj)

# nx.draw_networkx(G, arrows=True)
# plt.show()