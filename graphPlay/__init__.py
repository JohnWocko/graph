from graph import Graph
import graph_algorithms

g = Graph(3)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 3)
g.add_node('h')
g.add_value(0, 0)
g.add_edge(4, 5)

print(g, g.get_degree(0),'\n', g.get_degree_set())

graph_algorithms.dfs(g,'h')
graph_algorithms.extended_dfs(g,'h')
g.display_adj_list()
g.display_adj_matrix()
graph_algorithms.mitm_algorithm(g)