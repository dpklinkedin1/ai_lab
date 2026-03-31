def bfs_recu(Q, visited, graph):
    if len(Q) == 0:
        return
    current_node = Q.pop(0)
    
    if current_node not in visited:
        print(current_node)
        visited.append(current_node)
        for connected in graph.get(current_node, []):  # ← FIXED HERE
            if connected not in visited:
                Q.append(connected)
    bfs_recu(Q, visited, graph)


graph = {}

n = int(input("Enter number of nodes: "))
for i in range(n):
    node = int(input("Enter node: "))
    neighbors = list(map(int, input("Enter neighbors (space separated, leave empty if none): ").split()))
    graph[node] = neighbors

start_node = int(input("Enter starting node: "))

Q = [start_node]
visited = []
print("\nBFS Traversal:")
bfs_recu(Q, visited, graph)
