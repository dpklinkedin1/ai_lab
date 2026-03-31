from itertools import permutations

def tsp(graph, start):
    cities = list(range(len(graph)))
    cities.remove(start)

    min_cost = float('inf')
    best_path = []

    for perm in permutations(cities):
        cost = 0
        k = start

        for city in perm:
            cost += graph[k][city]
            k = city

        cost += graph[k][start]

        if cost < min_cost:
            min_cost = cost
            best_path = (start,) + perm + (start,)

    print("Minimum cost:", min_cost)
    print("Best path:", best_path)

graph = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

tsp(graph, 0)
