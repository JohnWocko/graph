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


# Sourced from https://www.geeksforgeeks.org/detect-cycle-in-a-graph/#:~:
# text=To%20detect%20cycle%2C%20check%20for,a%20cycle%20in%20the%20tree.
def isCyclicUtil(graph, v, visited, recStack):

       # Mark current node as visited and
       # adds to recursion stack
       visited[v] = True
       recStack[v] = True

       # Recur for all neighbours
       # if any neighbour is visited and in
       # recStack then graph is cyclic
       for i,neighbour in enumerate(graph.node_list[v][0]):
           if visited[i] == False:
               if isCyclicUtil(graph, i, visited, recStack) == True:
                   return True
           elif recStack[i] == True:
               return True

        # The node needs to be poped from
        # recursion stack before function ends
       recStack[v] = False
       return False

    # Returns true if graph is cyclic else false
def isCyclic(graph):
        visited = [False] * (graph.size + 1)
        recStack = [False] * (graph.size + 1)
        for node in range(graph.size):

            if visited[node] == False:
                if isCyclicUtil(graph,node,visited,recStack) == True:
                    return True
        return False






def mitm_algorithm(graph):
    start = 1
    end = graph.size-2
    vertices= graph.get_vertex_list()
    print(vertices)

    colours = OrderedDict()
    colours[0] = graph.node_list[start]

    if graph.size > 1:
        colours[1] = graph.node_list[start]

    while start <= end: # middle == graph.size/2
        print(graph.node_list[start][0], type(graph.node_list[start][0]),colours[1][0], type(colours[1]))
        if graph.get_degree(start) == 0 or graph.node_list[start][0].isdisjoint(colours[1][0]) :
            print(graph.node_list[start])
            print(colours[6])
        end-=1

