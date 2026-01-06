from collections import deque

graph = {
    "zero": {"one", "four"},
    "one": {"zero", "two", "three", "four"},
    "two": {"one", "three"},
    "three": {"one", "two", "four"},
    "four": {"zero", "one", "three"},
}

def bfs(vertex: str) -> list[str]:
    visited = []
    queue = deque()
    queue.append(vertex)
    while queue:
        neighbors = sorted(graph.get(queue[0]))
        for neighbor in neighbors:
            if neighbor not in visited and neighbor not in queue:
                queue.append(neighbor)
        visited.append(queue.popleft())
    
    return visited

def dfs(vertex: str, visited: set[str] | None = None):
    if visited is None:
        visited = set()

    if vertex not in graph:
        print("\nItem not present\n")
        return
    visited.add(vertex)
    for connected_vertex in sorted(graph.get(vertex)):
        if connected_vertex not in visited:
            dfs(connected_vertex, visited)
    print(visited)
    

dfs("zero")
