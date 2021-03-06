from graph import Graph
import graph_algorithms
import random
import os
graphs = []


def create_graph(graphs):
    if len(graphs) == 0:
        print('\n No graphs stored...')

    answer = str(input('\nCreate a Graph using input? - C\nCreate a random Graph? - R\nCreate the Soifer Graph? - S\nCreate Fib Graph? - '
    +'F\nReturn to main menu - Q\n'))

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
            print('Invalid Input')
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
        s = Graph.read_graph({0:[{1,2,3,7},[]], 1: [{2,4,8},[] ], 2: [{3,4,5},[] ], 3: [{5,6,7},[] ], 4: [{5,8},[] ],
                 5: [{6,8},[]], 6: [{7,8},[]], 7: [{8},[]]})

        graphs.append(s)

    if answer.upper() == 'Q':
        print(Graph.__doc__,*graphs)

def console():

    while (True):
        print('\n-----------------'
        +'\n\tMain Menu\n-----------------'
        +'\n\nCreate Graph? - (C)'
        +'\nView all Graphs via Adjacency List? - (V)'
        +'\nView all Graphs via Adjacency Matrix? - (M)'
        +'\nView all Graphs via networkx module visualisation? - (N)'
        +'\nColour all Graphs via MITM Algorithm? - (A)'
        +'\nColour Simulations? - (CS)'
        +'\nSave Graphs? - (S)'
        +'\nLoad Graphs? - (L)'
        +'\nClear Graphs? - (D)'
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
            quit()

        if choice.upper() == 'C':
            create_graph(graphs)

        if choice.upper() == 'V':
            for graph in graphs:
                print(graph)
                graph.display_adj_list()

        if choice.upper() == 'A' and len(graphs) != 0:
            for graph in graphs:
                print(f'\nRunning graph colouring algorithms on following Graph:\n{graph}\nMITM Algorithm:')
                colours = graph_algorithms.mitm_algorithm(graph)
                graph_algorithms.get_colouring(colours)
                graph.convert(colours)

                print(f'\nGreedy colouring:\t{graph}')
                colours2 = graph_algorithms.greedy_colouring(graph)
                graph_algorithms.get_colouring(colours2)
                graph.convert(colours2)

                print(f'\nSuper lazy colouring:\t{graph}')
                colours3 = graph_algorithms.super_lazy_colouring(graph)
                graph_algorithms.get_colouring(colours3)
                graph.convert(colours3)



        if choice.upper() == 'CS':
            try:
                for i in range(int(input('\nPlease enter a lower limit ')),int(input('\nplease enter an upper limit'))):
                    if  i == 0:
                        continue
                    else:
                        f = Graph.fib_graph(int(i*1.5))
                        graphs.append(f)
            except:
                print('Invalid Input:\nInput not an int')
            else:
                for graph in graphs:
                    print(graph)
                    graph_algorithms.mitm_algorithm(graph)


        if choice.upper() == 'D':
            try:
                graphs.clear()
            except:
                print('Could not delete graphs')
            else:
                print('Graphs emptied\n')

        if choice.upper() == 'S':
            try:
                for graph in graphs:
                    graph.save_to_file()
            except:
                print('Not able to save graphs')
            else:
                print('Save achieved!')

        if choice.upper() == 'L':
            try:
                if os.path.isfile("C:/Users/jon_w/PycharmProjects/pythonProject/graphPlay/graphs.txt"):
                    with open('graphs.txt', 'r') as f:
                        lines = f.readlines()
                    for line in lines:
                        graphs.append(Graph.read_graph(line))
                else:
                    print('No file to load from\n')

            except:
                print('Issue loading graph(s) from file\n')

            else:
                print('Graph loaded:')
                print(*graphs, graphs[0].size)


if __name__ == '__main__':
    console()



graph_algorithms.simple_search(graphs[1],'h')
graph_algorithms.binary_search(graphs[1],8)
graph_algorithms.improved_binary_search(graphs[1].node_list,8)
graph_algorithms.improved_binary_search({1,2,5,7,4,3,56,7},7)
graph_algorithms.bfs(graphs[1],6,  4)
graph_algorithms.dfs(graphs[1],6)

for node in graphs[1].node_list:
    print('\n------------------------')
    print(node,'\nbfs:', end=' ')
    graph_algorithms.bfs(graphs[1],1,  node)
    print('\ndfs:', end=' ')
    graph_algorithms.dfs(graphs[1],node, set())
    print('\n------------------------')




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