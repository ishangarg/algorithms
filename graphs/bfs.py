graph = {
    'a':['c', 'b'],
    'b': ['d'],
    'c': ['e'],
    'd': ['f'],
    'e': [],
    'f': []
}

def bradthFirstSearch(graph, node):
    queue = [node]

    while queue:
        curr_node = queue.pop(0)
        print(curr_node)
        for n in graph[curr_node]:
            queue.append(n)

bradthFirstSearch(graph, 'a')