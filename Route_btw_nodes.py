from collections import deque

def search(graph: dict, start: str, destination: str) -> bool:
    '''
    :param g: List of Lists. Shows the direction between the nodes.
    :return: Binary value
    '''

    visit = set()
    q = deque([start])
    while q:
        node = q.popleft()
        if node in visit:
            continue
        visit.add(node)
        if node == destination:
            return True
        for i in graph[node]:
            q.append(i)
    return False


graph = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['E', 'A'],
    'D': ['F'],
    'E': ['H', 'C'],
    'H': ['G'],
    'G': ['C'],
    'F': []
}
start = 'A'
destination = 'F'


print(search(graph, 'A', 'F'))  # True
print(search(graph, 'A', 'E'))  # True
print(search(graph, 'B', 'E'))  # False
print(search(graph, 'F', 'E'))  # False