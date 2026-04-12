from collections import deque

def water_jug_bfs(jug_a_cap, jug_b_cap, target):
    # Start state: both jugs empty
    start = (0, 0)
    
    # Queue for BFS: stores (current_state, path_taken)
    queue = deque()
    queue.append((start, [start]))
    
    # Visited set to avoid repeating states
    visited = set()
    visited.add(start)
    
    print(f"Jugs: A={jug_a_cap}L, B={jug_b_cap}L | Target: {target}L\n")
    
    while queue:
        (a, b), path = queue.popleft()
        
        # Check if goal is reached
        if a == target or b == target:
            print("Goal Reached!")
            print("\nStep-by-step Path:")
            for step, state in enumerate(path):
                print(f"  Step {step}: Jug A = {state[0]}L, Jug B = {state[1]}L")
            return path
        
        # Generate all possible next states
        next_states = [
            (jug_a_cap, b),           # Fill A
            (a, jug_b_cap),           # Fill B
            (0, b),                   # Empty A
            (a, 0),                   # Empty B
            # Pour A → B
            (a - min(a, jug_b_cap - b), b + min(a, jug_b_cap - b)),
            # Pour B → A
            (a + min(b, jug_a_cap - a), b - min(b, jug_a_cap - a)),
        ]
        
        for state in next_states:
            if state not in visited:
                visited.add(state)
                queue.append((state, path + [state]))
    
    print(" No solution found.")
    return None

# Run the program
water_jug_bfs(4, 3, 2)
