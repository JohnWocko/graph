import sys
import networkx as nx
import random
from random import randint
import ast
import matplotlib.pyplot as plt
import os


class Graph:
    """
    A class to represent a Graph using a linked list like structure. It's structure is based within a dictionary,
    where each key is a vertex and the value is a list that has two nested lists. the first nested list represents
    vertices adjacent, the second is for data to be stored.

    ...

    Attributes
    ----------
    node_list : set
        Contains all nodes within a dictionary to represent a graph structure. Each key: value pair represents a
        key/vertex/node paired with a value/list. Within this list are two items. Firstly a set to represent unique
        adjacent vertices and then secondly, a list to hold data for the key node --> Node:[Adjacency set(), Data []]
    size : int
        This can be set when graph is created, or is based upon the length of keys within the node_list which can be
        based on string characters.


    Methods
    -------
    info(additional=""):
        Prints the person's name and age.
    """


    def __init__(self, size = 0):
        '''     '''
        # Stored in a linkedlist type structure, where the dictionary key is a vertex and the value
        # is a list containing two data objects: the first being a set that represents the vertices
        # connected to this key vertex, and the second that can store data values within a list

        # To access a node - node_list[node]
        # To access a nodes adj list, - node_list[node][0]
        # To access a nodes values, - node_list[node][1]

        self.node_list = {}
        self.size = size

        # Sets the value of each node within the dictionary to an empty set called node_list
        # and a list to store values, the adjacent values will be added
        # upon object creation. If an int is passed-in, then up to that number of nodes will be created or if a
        # string is passed in, each individual char becomes a node.

        if isinstance(self.size, int) :
            for node in range(self.size):
                self.node_list[node] =[set(), []]
        else:
            for node in self.size:
                self.node_list[node] =[set(), []]

    # Returns the graph size and its Adjacency list
    def __str__(self):
        '''     '''
        return f'\nGraph of size: {self.size} \n{self.node_list }'

    def __del__(self):
        '''     '''
        del  self.node_list, self.size

    def __size__(self):
        '''     '''
        return len(self.node_list)

    def __call__(self, *args):
        '''     '''
        temp_node_list = []
        for arg in args:
            temp_node_list.append(self.node_list[arg])
        return temp_node_list

    def __lt__(self, object2):
        '''     '''
        return self.size < object2.size

    def __gt__(self, object2):
        '''     '''
        return self.size > object2.size

    def __le__(self, object2):
        '''     '''
        return self.size <= object2.size

    def __ge__(self, object2):
        '''     '''
        return self.size >= object2.size

    def __eq__(self, object2):
        '''     '''
        return self.node_list == object2.node_list

    def __ne__(self, object2):
        '''     '''
        return self.node_list != object2.node_list

    def node_check(self, node):
        '''     '''
        return node in self.node_list

    def edge_check(self, node, edge):
        '''     '''
        return edge in self.node_list[node][0]


    # Method to add an edge to a vertexs' adjacency list
    def add_edge(self, node, edge, directed = False):
        '''     '''
        # Undirected OR directed Graph with no self=cycles - So will only add if not already
        # adjacent and the use object of a set means no duplicates and it will retain order
        if not self.node_check(node):
            self.add_node(node)

        if not self.node_check(edge):
            self.add_node(edge)

        if edge != node and directed == False:
            self.node_list[node][0].add(edge)
            self.node_list[edge][0].add(node)

        elif edge != node and directed == True:
            self.node_list[node][0].add(edge)
        else:
            print('Error - Unable to add edge')

    # Used to add a node to the graph structure with a default empty value list or with a value list
    def add_node(self, node, value = None):
        '''     '''
        if not self.node_check(node):
            if value is None:
                self.node_list[node] = [set(),[]]
                self.size +=1
            else:
                self.node_list[node] = [set(),[value]]
                self.size +=1
        else:
            print('Error adding node, already exists')

    def get_degree(self, node):
        '''     '''
        return len(self.node_list[node][0])

    def get_degree_set(self):
        '''     '''
        degree_set = []
        for node in self.node_list:
            degree_set.append(self.get_degree(node))
        return degree_set

    # needs to be updated to account for empty sets
    def max_degree(self):
       '''     '''
       degree_set = self.get_degree_set()
       max_degree =0
       location = ''
       keys = list(self.node_list.keys())

       for i,degree in enumerate(degree_set):
           if degree > max_degree:
                max_degree = degree
                location = i
       print(f'Max degree of {max_degree} at index {location} or vertex {keys[location]}')
       return keys[location], max_degree

    def min_degree(self):
       '''     '''
       degree_set = self.get_degree_set()
       min_degree =sys.maxsize
       location = ''
       keys = list(self.node_list.keys())

       for i,degree in enumerate(degree_set):
           if degree < min_degree:
                min_degree = degree
                location = i
       print(f'Min degree of {min_degree} at index {location} or vertex {keys[location]}')
       return keys[location], min_degree

    def get_adj_vertices(self, vertex):
        '''     '''
        vertex_list = []
        for node in self.node_list[vertex][0]:
            vertex_list.append(node)
        return vertex_list

    def get_vertex_list(self):
        '''     '''
        vertex_list = []
        for node in self.node_list:
            vertex_list.append(node)
        return vertex_list


    # Used to remove an edge from a vertices adjacency list
    def remove_edge(self, node, edge):
        '''     '''
        if not self.edge_check(node, edge):
            self.node_list[node][0].remove(edge)
            self.node_list[edge][0].remove(node)

    # Removes a node and its adjacency list from the graph structure and all
    # mentions of it in other adjacency list entries
    def remove_node(self, node):
        '''     '''
        if self.node_check(node):
            for other_node in self.node_list:
               # print('here ',other_node, node, self.node_list[other_node][0])
                if self.edge_check(node, other_node):
                    self.remove_edge(other_node, node)
            self.node_list.pop(node)
            self.size -=1
        else:
            print( f'Vertex/Node: {node} does not appear in graph.')


    def add_value(self, node, value):
        '''     '''
        if node in self.node_list:
            self.node_list[node][1].append(value)

    def display_adj_list(self):
        '''     '''
        print('\nAdjacency List')
        for node in self.node_list:
            print('\t',node,'-->',self.node_list[node][0])

    def get_nodes(self):
        '''     '''
        all_nodes = []
        for node in self.node_list:
            all_nodes.append(node)
        return all_nodes

    def display_adj_matrix(self):
        '''     '''
        print('\nAdjacency Matrix')
        for node in self.node_list:
            print('\n',node,'|| ', end='')
            for other_node in self.node_list:
                if self.edge_check(node,other_node):
                    print(' X |', end='')
                else:
                    print(' - |', end='')

    def convert(self, colours=1):
        '''     '''
        graph = nx.Graph()

        color_list = []
        colour_list = []

        if colours ==   1:
            for node in self.node_list:
                #graph.add_node(node)
                for connected_node in self.node_list[node][0]:
                    graph.add_edge(node,connected_node)
            nx.draw(graph, node_color = '#%06X' % randint(0, 0xFFFFFF), with_labels=True)

        elif isinstance(colours, dict):
            for i in range(len(colours)):
                color_list.append('#%06X' % randint(0, 0xFFFFFF))
            for node in self.node_list:
                #graph.add_node(node)
                for connected_node in self.node_list[node][0]:
                    graph.add_edge(node,connected_node)

            for g_node in graph.nodes():
                for colour in colours.keys():
                    if g_node in colours[colour]:
                        colour_list.append(color_list[colour])
            nx.draw(graph,node_color=colour_list, with_labels=True)
        plt.show()


    def is_fibbinary_num(n):
        '''     '''
        if(int(n) & (int(n)>>1) == 0):
            return True
        else:
            return False

    def hamming_distance(num1, num2):
        '''     '''
        x = num1 ^ num2
        set_bits = 0

        while (x > 0):
            set_bits += x & 1
            x >>= 1
        return set_bits

    def fib_graph(nodes):
        '''     '''
        fib_graph = Graph(nodes)
        for i in range(0, nodes + 1):
            if not Graph.is_fibbinary_num(i):
                continue
            for j in range(0, nodes + 1):
                if not Graph.is_fibbinary_num(j):
                    continue
                elif ((Graph.hamming_distance(i,j) == 1 )):
                    fib_graph.add_edge(i,j)

        return fib_graph

    def read_graph(graph_structure):
        '''     '''
        if  isinstance(graph_structure, str):
            return Graph.read_graph(ast.literal_eval(graph_structure))
        else:

            if isinstance(graph_structure, dict):
                imported_graph = Graph()

                if len(graph_structure.keys()) == 2 :
                    for key in graph_structure.keys():
                        imported_graph.add_node(key)

                        for node in graph_structure[key][0]:
                            imported_graph.add_edge(key, node)

                        if (graph_structure[key][1]) != '[]':
                            for data in graph_structure[key][1]:
                                imported_graph.add_value(key, data)

                        else:
                            imported_graph.add_value(key, '')
                else:
                    for key in graph_structure.keys():
                        imported_graph.add_node(key)

                        for node in graph_structure[key][0]:
                            imported_graph.add_edge(key, node)
                return imported_graph



    def save_to_file(self):
        '''     '''
        if not os.path.isfile("C:/Users/jon_w/PycharmProjects/pythonProject/graphPlay/graphs.txt"):
            with open('graphs.txt', 'w') as f:
                f.write(str(self.node_list))
                f.write('\n')
        else:
            with open('graphs.txt', 'a') as f:
                f.write(str(self.node_list)+'\n')


