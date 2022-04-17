from graph import Graph
import graph_algorithms

g = Graph()
g.add_edge(0, 1, True)

g.add_edge(2, 3, True)
g.add_node('h')
g.add_edge(3, 'h')

g.add_edge('h', 5, False)



graph_algorithms.dfs(g,'h')
graph_algorithms.extended_dfs(g,'h')
g.display_adj_list()
g.display_adj_matrix()

print(graph_algorithms.isCyclic(g))
#graph_algorithms.mitm_algorithm(g)
print('\n',g, g.max_degree(), g.min_degree())