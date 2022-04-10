

'''



'''


# Graph structure class
class Graph:
    def __init__(self, nodes=1):
        # Stored in a linkedlist type structure, where the dictionary key is a vertex and the value
        # is a list containing two data objects: the first being a set that represents the vertices
        # connected to this key vertex, and the second that can store data values within a list

        # To access a node use node_list[node]
        # To access a nodes adj list, use node_list[node][0]
        # To access a nodes values, use node_list[node][1]

        self.node_list = {}
        self.nodes = nodes
        self.size = 0

        # Sets the value of each node within the dictionary to an empty node_list
        # and a list to store values, the adjacent values will be added
        # upon object creation

        if isinstance(self.nodes, int) :
            for node in range(self.nodes):
                self.node_list[node] =[set(), []]
                self.size +=1
        else:
            for node in self.nodes:
                self.node_list[node] =[set(), []]
                self.size +=1
    # Returns the graph size and its Adjacency list
    def __str__(self):
        return f'\nGraph of size: {self.size} \n{self.node_list }'

    def __del__(self):
        del  self.node_list, self.nodes, self.size

    def __call__(self, *args):
        temp_node_list = []
        for arg in args:
            temp_node_list.append(self.node_list[arg])
        return temp_node_list

    def __lt__(self, object2):
        return self.size < object2.size
    def __gt__(self, object2):
        return self.size > object2.size
    def __le__(self, object2):
        return self.size <= object2.size
    def __ge__(self, object2):
        return self.size >= object2.size
    def __eq__(self, object2):
        return self.node_list == object2.node_list
    def __ne__(self, object2):
        return self.node_list != object2.node_list

    def node_check(self, node):
        return node in self.node_list

    def edge_check(self, node, edge):
        return edge in self.node_list[node][0]


    # Method to add an edge to a vertexs' adjacency list
    def add_edge(self, node, edge, directed = False):
        # Undirected OR directed Graph with no self=cycles - So will only add if not already
        # adjacent and the use object of a set means no duplicates and it will retain order
        if not self.node_check(node):
            self.add_node(node)
        elif not self.node_check(edge):
            self.add_node(edge)

        if edge != node and directed ==False:
            self.node_list[node][0].add(edge)
            self.node_list[edge][0].add(node)

        elif edge != node and directed == True:
            self.node_list[node][0].add(edge)
        else:
            print('Error - Unable to add edge')

    # Used to add a node to the graph structure with a default empty value list or with a value list
    def add_node(self, node, value = None):
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
        return len(self.node_list[node][0])

    def get_degree_set(self):
        degree_set = []
        for node in self.node_list:
            degree_set.append(self.get_degree(node))
        return degree_set


    def get_vertex_list(self):
        vertex_list = []
        for node in self.node_list:
            vertex_list.append(node)
        return vertex_list


    # Used to remove an edge from a vertices adjacency list
    def remove_edge(self, node, edge):
        if not self.edge_check(node, edge):
            self.node_list[node][0].remove(edge)
            self.node_list[edge][0].remove(node)

    # Removes a node and its adjacency list from the graph structure and all
    # mentions of it in other adjacency list entries
    def remove_node(self, node):
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
        if node in self.node_list:
            self.node_list[node][1].append(value)

    def display_adj_list(self):
        print('Adjacency List')
        for node in self.node_list:
            print('\t',node,'-->',self.node_list[node][0])

    def display_adj_matrix(self):
        print('Adjacency Matrix')
        for node in self.node_list:
            print('\n',node,'|| ', end='')
            for other_node in self.node_list:
                if self.edge_check(node,other_node):
                    print(' X |', end='')
                else:
                    print(' - |', end='')

    def cycle_check(self, vertex):
        for node in self.node_list[vertex][0]:
            if vertex in self.node_list[node][0]:
                print(f'\nvertex {vertex} has a cycle with vertex {node}', end = ' ' )
                #return True #vertex in self.node_list[node]

            else:  #
                self.cycle_check(node)

        print(f'\nNo cycle detected for vertex {vertex}',end = ' ')
        return False

    def graph_cyclic(self):
        for node in self.node_list:
            self.cycle_check(node)


g = Graph(4)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 3)
g.add_edge(0, 'h')
g.add_edge(0, 'f', True)
g.display_adj_list()
g.display_adj_matrix()
g.cycle_check('f')
g.graph_cyclic()
g.add_edge('f', 'h', True)
g.display_adj_matrix()
g.graph_cyclic()