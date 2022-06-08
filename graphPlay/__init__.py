from graph import Graph
import graph_algorithms
import random
graphs = []


def create_graph(graphs):
    if len(graphs) == 0:
        print('\n No graphs stored...')

    answer = str(input('\nCreate a random Graph? - R\nCreate the Soifer Graph? - S\nCreate Fib Graph? - '
    +'F\nReturn to main menu - Q'))

    if answer.upper() == 'R':
        try:
            randNode = random.randint(3, int(input('\nRandom upper limit? - (3 - 100)')))
        except:
            print('Invalid Input:\nInput not an int')
            create_graph(graphs)
        else:
            g = Graph(randNode)
            for node in g.node_list:
                if bool(random.getrandbits(1)):
                    for other_node in g.node_list:
                        if bool(random.getrandbits(1)):
                            g.add_edge(node, other_node)
                        else:
                            continue
                else:
                    continue
        graphs.append(g)

    if answer.upper() == 'C':
        try:
            created_graph = Graph()
            print('Please enter a node list in the form \'1234\' where each character signifies a node/vertex:\n')
            nodes = input('Please enter node list:\n')
            for node in sorted(nodes):
                created_graph.add_node(node)
            for node in created_graph.node_list:
                print(f'{created_graph}\nPlease enter the nodes connected to vertex {node} in the form \'1234\' where each number signifies an adjacent node/vertex:\n')
                adjacent_nodes = input('Please enter adjacent node list:\n')
                for adj_node in sorted(adjacent_nodes):
                    if created_graph.node_check(adj_node):
                        created_graph.add_edge(node, adj_node)
                    else:
                        print('You\'ve put in a node that isn\'t in the graph')
        except:
            print('Invalid Input:\nInput not an int')
            create_graph(graphs)
        else:
            print(created_graph)
        graphs.append(created_graph)

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

    if answer.upper() == 'Q':
        print(*graphs)

def console():

    while (True):
        print('\n-----------------'
        +'\n\tMain Menu\n-----------------'
        +'\n\nCreate Graph? - (C)'
        +'\nView all Graphs via Adjacency List? - (V)'
        +'\nView all Graphs via Adjacency Matrix? - (M)'
        +'\nView all Graphs via networkx module visualisation? - (N)'
        +'\nColour all Graphs via MITM Algorithm? - (A)'
        +'\nColour Simulations? - (S)'
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
        if choice.upper() == 'A' and len(graphs) != 0:
            for graph in graphs:
                print(graph)
                graph_algorithms.mitm_algorithm(graph)

        if choice.upper() == 'S':
            try:
                for count,i in enumerate(range(int(input('\nPlease enter a lower limit ')),int(input('\nplease enter an upper limit')))):
                    if count == 0 or i == 0:
                        continue
                    else:
                        f = Graph.fib_graph(i*count)
                        graphs.append(f)
            except:
                print('Invalid Input:\nInput not an int')
            else:
                for graph in graphs:
                    print(graph)
                    graph_algorithms.mitm_algorithm(graph)


console()
graph_algorithms.dfs(graphs[0],'h')
graph_algorithms.extended_dfs(graphs[0],'h')


print(graph_algorithms.isCyclic(graphs[0]))
""" graph1 = Graph.read_graph({0:[[1],['hello']]})
graph2 = Graph.read_graph({0:[[1]]})
graph3 = Graph.read_graph({0:[[x for x in range(0,10)]],1:[[x for x in range(0,10)]],2:[[x for x in range(0,10)]],
3:[[x for x in range(0,10)]],4:[[x for x in range(0,10)]],5:[[x for x in range(0,10)]], 6:[[1,6,8,4]]})

graph4 = Graph.read_graph('{0:[[1,2,3,4,5,6,78],[\'hfghfghfghfg\']], 5:[[1,6,8,4],[\'hi\']]}')
graphs.append(graph1)

graphs.append(graph3)
graphs.append(graph2)
graphs.append(graph4)
print('Here ',graph4) """

"""
for graph in graphs:
    print(graph)
    graph_algorithms.mitm_algorithm(graph)
    graph.convert()
 """


"""

g = graphs[0]
print(g)

graph_algorithms.dfs(g,'h')
graph_algorithms.extended_dfs(g,'h')


print(graph_algorithms.isCyclic(g))
graph_algorithms.mitm_algorithm(graphs[0])
graph_algorithms.mitm_algorithm(graphs[1])
print('\n',g, g.max_degree(), g.min_degree())

"""