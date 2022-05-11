from graph import Graph
import graph_algorithms
import random
graphs = []
f = Graph.fib_graph(100)
graphs.append(f)
def create_graph(graphs):
    if not graphs:
        print('\n No graphs stored...')
        answer =str(input('\nCreate a random one? Y/N'))

        if answer.upper() == 'Y':
            randNode = random.randint(0,20)
            g = Graph(randNode)

            for node in g.node_list:
                for other_node in g.node_list:
                    if ((node + other_node) % 3 == 0):
                         g.add_edge(node, other_node)


            g.add_edge(0, 1, True)
            g.add_edge(2, 3, True)
            g.add_node('h')
            g.add_edge(3, 'h')

            graphs.append(g)

            g2 = Graph()
            g2.add_edge(0, 1, True)
            g2.add_edge(2, 1, True)
            g2.add_node('h')
            g2.add_edge(3, 'h')
            g2.add_edge('h', 5, False)
            graphs.append(g2)


def console():
    create_graph(graphs)
    while (True):
        print('\n-----------------'
        +'\n\tMain Menu\n-----------------')

        print('')

        choice = str(input('\nPlease enter an option:\n'))
        if (choice.upper() =='M'):
            for graph in graphs:
                graph.convert()
                graph.display_adj_matrix()



console()




print(g)

graph_algorithms.dfs(g,'h')
graph_algorithms.extended_dfs(g,'h')
g.display_adj_list()
g.display_adj_matrix()

print(graph_algorithms.isCyclic(g))
#graph_algorithms.mitm_algorithm(g)
print('\n',g, g.max_degree(), g.min_degree())
