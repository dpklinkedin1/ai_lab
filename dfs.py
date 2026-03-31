def dfs_recu(current_node, visited, graph):
    if current_node in visited:
        return
    print(current_node)
    visited.append(current_node)
    for connected in graph.get(current_node, []):  # ← FIXED
        dfs_recu(connected, visited, graph)


graph = {}

n = int(input("Enter number of nodes: "))
for i in range(n):
    node = int(input("Enter node: "))
    neighbors = list(map(int, input("Enter neighbors (space separated, leave empty if none): ").split()))
    graph[node] = neighbors

start_node = int(input("Enter starting node: "))

visited = []
print("\nDFS Traversal:")
dfs_recu(start_node, visited, graph)
