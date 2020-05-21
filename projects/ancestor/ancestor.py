from util import Queue, Graph


def earliest_ancestor(ancestors, starting_node):
    '''
    Build the graph
    '''
    # instantiate a new graph object
    graph = Graph()
    # loop over all pairs in ancestors
    for pair in ancestors:
        # add pair[0] and pair[1] to the graph
        graph.add_vertex(pair[0])
        graph.add_vertex(pair[1])
        # build the edges in reverse
        graph.add_edge(pair[1], pair[0])
    '''
    BFS with paths to find the earliest known ancestor
    '''
    # create a queue
    queue = Queue()
    # enqueue starting node inside a list
    queue.enqueue([starting_node])
    # set a max path length to 1
    max_path_length = 1
    # set initial earliest ancestor
    earliest_ancestor = -1
    # while the queue is not empty
    while not queue.is_empty():
        # dequeue to the path
        path = queue.dequeue()
        # set a vertex to the last item in the path
        vertex = path[-1]
        # if path is longer or equal and the value is smaller, or if the path is longer
        if (len(path) >= max_path_length and vertex < earliest_ancestor) or (len(path) > max_path_length):
            # set the earliest ancestor to the vertex
            earliest_ancestor = vertex
            # set the max path length to the len of the path
            max_path_length = len(path)
        # loop over next vertex in the set of vertices for the current vertex
        for next_vertex in graph.vertices[vertex]:
            # set a new path equal to a new list of the path
            path_copy = list(path)
            # append next vertex to new path
            path_copy.append(next_vertex)
            # enqueue the new path
            queue.enqueue(path_copy)
    # return earliest ancestor
    return earliest_ancestor
