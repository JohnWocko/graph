from graph import Graph
import graph_algorithms
import random
graphs = []


def create_graph(graphs):
    if not graphs:
        print('\n No graphs stored...')

        f = Graph.fib_graph(int(input('\nFib num? - (0 - 10000)'))+1)
        f.add_edge(0,'h')
        graphs.append(f)


        answer =str(input('\nCreate a random one? - R\nCreate the Soifer Graph? - S'))

        if answer.upper() == 'R':
            randNode = random.randint(0,20)
            g = Graph(randNode)

            for node in g.node_list:
                for other_node in g.node_list:
                    if ((node + other_node) % 3 == 0):
                         g.add_edge(node, other_node)


            graphs.append(g)

            g2 = Graph()
            g2.add_edge(0, 1, True)
            g2.add_edge(2, 1, True)
            g2.add_node('h')
            g2.add_edge(3, 'h')
            g2.add_edge('h', 5, False)
            graphs.append(g2)

        if answer.upper() == 'S':
            s = Graph()
            s.add_edge(0,1)
            s.add_edge(0,3)
            s.add_edge(0,7)
            s.add_edge(0,2)
            s.add_edge(1,2)
            s.add_edge(1,4)
            s.add_edge(1,8)
            s.add_edge(2, 3)
            s.add_edge(2, 4)
            s.add_edge(2, 5)
            s.add_edge(3, 5)
            s.add_edge(3, 6)
            s.add_edge(3, 7)
            s.add_edge(4, 5)
            s.add_edge(4, 8)
            s.add_edge(5, 6)
            s.add_edge(5, 8)
            s.add_edge(6, 7)
            s.add_edge(6, 8)
            s.add_edge(7, 8)
            graphs.append(s)
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
        if (choice.upper() =='Q'):
            break



console()



g = graphs[0]
print(g)

graph_algorithms.dfs(g,'h')
graph_algorithms.extended_dfs(g,'h')


print(graph_algorithms.isCyclic(g))
graph_algorithms.mitm_algorithm(graphs[0])
graph_algorithms.mitm_algorithm(graphs[1])
print('\n',g, g.max_degree(), g.min_degree())
