# A function used by dfs

import collections

try:
    from collections import OrderedDict
except ImportError:
    OrderedDict = dict
def dfs_util(graph, v, visited):
        # Mark the current node as visited
        # and print it
        if v not in visited and v in graph.node_list.keys():
            visited.add(v)
            print(v, end='  ')

            # Recur for all the vertices
            # adjacent to this vertex

            for node in graph.node_list[v][0]:
                if node not in visited:
                    dfs_util(graph,node, visited)



    # The function to do dfs traversal. It uses
    # recursive dfs_util()
def dfs(graph, v):

        # Create a set to store visited vertices
        visited = set()

        if v not in graph.node_list.keys():
           print('Not in graph')
        else:
            # Call the recursive helper function
            # to print dfs traversal
            dfs_util(graph, v, visited)
        print('')



def extended_dfs(graph, v):
        if v not in graph.node_list.keys():
            print('Not in graph')
        else:
            # Create a set to store visited vertices and
            # a set to store those without edges
            visited = set()
            disconnected = set()

            # Call the recursive helper function
            # to print dfs traversal

            if len(graph.node_list[v][0] )<1:
                disconnected.add(v)
            dfs_util(graph, v, visited)

            # Checks to see if all nodes of the graph has been visited

            if visited != set(graph.node_list.keys()):
                print('Not all vertices explored - ', end = ' ')
                # If not, the unvisited nodes are added to a set to be transversed
                unvisited = set(graph.node_list.keys()).difference(visited)
                while (len(unvisited) >0):
                    v = unvisited.pop()
                    if graph.get_degree(v)<1:
                        disconnected.add(v)
                    dfs_util(graph,v, visited)


def bfs(graph, vertex):
    if v not in graph.node_list:
            print('Not in graph')
    else:
        queue = []
        explored = []

        explored.append(vertex)
        print(vertex, end = ' ')


# Algorithm designed for my BSc Computer Science project to colour graphs greedily, performs in Big O = On^2 Time
# so far has issues with graphs that doesn't have successive nodes
def mitm_algorithm(graph):
    start = 1
    end = graph.size-2
    vertices = sorted(graph.get_nodes())

    colours = OrderedDict()
    colours[0] = {vertices[0]}

    if graph.size > 1:
        colours[1] = {vertices[end+1]}
    while start <= end: # middle == graph.size/2
        if graph.get_degree(vertices[start]) == 0 or graph.node_list[vertices[start]][0].isdisjoint(colours[1]) :
            colours[1].add(vertices[start])
        elif graph.node_list[vertices[start]][0].isdisjoint(colours[0]):
            colours[0].add(vertices[start])

        else:
            colour = 0
            c = 0
            for i in range(len(colours)):
                if graph.node_list[vertices[start]][0].isdisjoint(colours[i]):
                    colours[i].add(vertices[start])
                    c = 1
                    break
            if c ==0:
                colours[len(colours)] = {vertices[start]}

        if start != end:
            print( vertices[end])
            if graph.get_degree(vertices[end]) == 0 or graph.node_list[vertices[end]][0].isdisjoint(colours[0]) :
                colours[0].add(vertices[end])
            elif graph.node_list[vertices[end]][0].isdisjoint(colours[1]):
                colours[1].add(vertices[end])

            else:
                colour = 0
                c = 0
                for i in range(len(colours)):
                    if graph.node_list[vertices[end]][0].isdisjoint(colours[i]):
                        colours[i].add(vertices[end])
                        c = 1
                        break
                if c ==0:
                    colours[len(colours)] = {vertices[end]}

        start +=1
        end-=1
    get_colouring(colours)

def get_colouring(colours):
    print(f'\nColouring of graph with {len(colours.keys())} colours:')
    for colour in colours.keys():
        print('\n',colour, end = ' --> ')
        for node in colours[colour]:
            print (node, end =' ')
    print('\n')
