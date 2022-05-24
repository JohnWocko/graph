from graph import Graph
import graph_algorithms
import random
graphs = []


def create_graph(graphs):
    if len(graphs) == 0:
        print('\n No graphs stored...')

    answer =str(input('\nCreate a random one? - R\nCreate the Soifer Graph? - S\nCreate Fib Graph? - F'))

    if answer.upper() == 'R':
        randNode = random.randint(0,20)
        g = Graph(randNode)

        for node in g.node_list:
            for other_node in g.node_list:
                if ((node + other_node) % 3 == 0):
                    g.add_edge(node, other_node)


        graphs.append(g)

    """     g2 = Graph()
        g2.add_edge(0, 1, True)
        g2.add_edge(2, 1, True)
        g2.add_node('h')
        g2.add_edge(3, 'h')
        g2.add_edge('h', 5, False)
        graphs.append(g2) """



    if answer.upper() == 'F':
        try:
            f = Graph.fib_graph(int(input('\nFib num? - (0 - 10000)')))
        except:
            print('Invalid Input:\nInput not an int')
        else:
            graphs.append(f)

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

    while (True):
        print('\n-----------------'
        +'\n\tMain Menu\n-----------------'
        +'\n\nCreate Graph? - (C)'
        +'\nView all Graphs via Adjacency List? - (V)'
        +'\nView all Graphs via Adjacency Matrix? - (M)'
        +'\nView all Graphs via networkx module visualisation? - (N)'
        +'\nColour all Graphs via MITM Algorithm? - (A)'
        +'\nExit? - (E)')

        print('')

        choice = str(input('\nPlease enter an option:\n'))
        if (choice.upper() =='M'  and len(graphs) != 0):
            for graph in graphs:
                graph.display_adj_matrix()
        if (choice.upper() =='N'  and len(graphs) != 0):
            for graph in graphs:
                graph.convert()
        if (choice.upper() =='E'):
            break
        if choice.upper() == 'C':
            create_graph(graphs)
        if choice.upper() == 'V':
            for graph in graphs:
                print(graph)
                graph.display_adj_list()
        if choice.upper() == 'A 'and len(graphs) != 0:
            for graph in graphs:
                print(graph)
                graph_algorithms.mitm_algorithm(graph)




console()



g = graphs[0]
print(g)

graph_algorithms.dfs(g,'h')
graph_algorithms.extended_dfs(g,'h')


print(graph_algorithms.isCyclic(g))
graph_algorithms.mitm_algorithm(graphs[0])
graph_algorithms.mitm_algorithm(graphs[1])
print('\n',g, g.max_degree(), g.min_degree())
