from networkx import connected_components, Graph, minimum_edge_cut
from math import prod

DEFAULT_INPUT = 'day25.txt'

def part_1(loc: str = DEFAULT_INPUT) -> int:
    nodes = set()
    edges = set()
    with open(loc) as f:
        for line in f.readlines():
            lhs, rhs = line.rstrip().split(': ')
            nodes.add(lhs)
            comps = rhs.split(' ')
            for comp in comps:
                nodes.add(comp)
                edges.add(tuple(sorted((lhs, comp))))
    graph = Graph()
    graph.add_nodes_from(nodes)
    graph.add_edges_from(edges)
    to_cut = minimum_edge_cut(graph)
    graph.remove_edges_from(to_cut)
    return prod(len(group) for group in connected_components(graph))

if __name__ == '__main__':
    print('Solution for Part One:', part_1())
