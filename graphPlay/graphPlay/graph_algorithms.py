import collections

try:
    from collections import OrderedDict
except ImportError:
    OrderedDict = dict

def simple_search(graph, target_node):
    return target_node in graph.node_list.keys()

def binary_search(graph, target_node):
    for node in graph.node_list:
        if target_node == node:
            print(f'{target_node} found in graph using basic binary search')
            return True
    return False

def improved_binary_search(node_list, target_node):
    mid  = int(len(node_list)/2)
    sorted_nodes = sorted(node_list)
    print(sorted_nodes)

    if len(sorted_nodes) >=2:
        if sorted_nodes[mid] == target_node:
            print(target_node, ' Found using Divide and conquer BS')
            return True
        elif sorted_nodes[mid] <= target_node:
            improved_binary_search(sorted_nodes[mid:], target_node)
        elif sorted_nodes[mid] >= target_node:
            improved_binary_search(sorted_nodes[:mid], target_node)
    else:
        print(target_node,' Not in graph')
        return False

def bfs(graph, starting_vertex, goal_vertex):
    if starting_vertex in graph.node_list:
        visited = set()
        queue = []
        visited.add(starting_vertex)
        queue.append(starting_vertex)

        print('Path taken: ',end ='')
        while queue:
            v = queue.pop(0)
            print(v,end= ' ')

            if v == goal_vertex:
                print(f'{v} found')
                return v
            for adj_node in graph.get_adj_vertices(v):
                if adj_node not in visited:
                    if adj_node in queue:
                        continue
                    else:
                        visited.add(adj_node)
                        queue.append(adj_node)
            #print('In the Q: ', queue,' V: ', visited)


    else:
        print(f'Starting vertex/index: {starting_vertex} not in graph.')
        return False

def dfs (graph, starting_vertex, visited =set()):
    if starting_vertex in graph.node_list:
            visited.add(starting_vertex)
            print(visited, end = ' ')
            for adj_node in graph.get_adj_vertices(starting_vertex):

                if adj_node not in visited:
                    print(' - ', adj_node)
                    dfs(graph, adj_node, visited)
                print(f'{adj_node } has been visited')



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
