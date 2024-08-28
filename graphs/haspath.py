graph = {
    'f':['g', 'i'],
    'g':['h'],
    'h': [],
    'i':['g','k'],
    'j':['i'],
    'k': []
}

def hasPathDFS(graph, src, dst):
    stack = [src]

    while stack:
        curr_node = stack.pop()

        for node in graph[curr_node]:
            if node == dst:
                return True
            
            stack.append(node)
    
    return False

def hasPathBFS(graph, src, dst):
    queue = [src]

    while queue:
        curr_node = queue.pop(0)

        for node in graph[curr_node]:
            if node == dst:
                return True
        
            queue.append(node)
    
    return False


print(hasPathBFS(graph, 'a', 'k'))