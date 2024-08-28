graph = {
    'a':['b', 'c'],
    'b': ['d'],
    'c': ['e'],
    'd': ['f'],
    'e': [],
    'f': []
}

def depthFirstPrint(graph, node):
    stack = [node]

    while stack:
        curr_node = stack.pop()
        print(curr_node)

        for n in graph[curr_node]:
            stack.append(n)

def depthFirstRecursion(graph, node):
    print(node)

    for n in graph[node]:
        depthFirstRecursion(graph, n)

depthFirstRecursion(graph, 'a')
