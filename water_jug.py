from collections import deque

def water_jug(j1, j2, target):
    visited = set()
    queue = deque([(0, 0, [])])

    while queue:
        a, b, path = queue.popleft()
        if (a, b) in visited:
            continue
        visited.add((a, b))
        path = path + [(a, b)]

        if a == target or b == target:
            for i, step in enumerate(path):
                print(f"Step {i}: Jug1={step[0]}L, Jug2={step[1]}L")
            return

        for na, nb in [
            (j1, b), (a, j2),             # Fill8
            (0, b),  (a, 0),              # Empty
            (a - min(a, j2-b), b + min(a, j2-b)),  # Pour 1→2
            (a + min(b, j1-a), b - min(b, j1-a)),  # Pour 2→1
        ]:
            if (na, nb) not in visited:
                queue.append((na, nb, path))

    print("Not possible.")

j1 = int(input("Jug1 capacity: "))
j2 = int(input("Jug2 capacity: "))
t  = int(input("Target: "))
water_jug(j1, j2, t)
