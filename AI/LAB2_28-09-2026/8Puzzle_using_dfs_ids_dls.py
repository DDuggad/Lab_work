import copy
INITIAL_STATE = (2, 8, 3, 1, 6, 4, 7, 0, 5)
GOAL_STATE = (1, 2, 3, 8, 0, 4, 7, 6, 5)

def print_state(state):
    for i in range(0, 9, 3):
        row = state[i:i+3]
        print(" ".join(str(x) if x != 0 else "_" for x in row))
    print()

def get_neighbors(state):
    neighbors = []
    blank_idx = state.index(0)
    row, col = divmod(blank_idx, 3)

    moves = {
        'Up': (row - 1, col),
        'Down': (row + 1, col),
        'Left': (row, col - 1),
        'Right': (row, col + 1)
    }

    for direction, (r, c) in moves.items():
        if 0 <= r < 3 and 0 <= c < 3:
            swap_idx = r * 3 + c
            # Create a new state by swapping the blank with the target tile
            new_state = list(state)
            new_state[blank_idx], new_state[swap_idx] = new_state[swap_idx], new_state[blank_idx]
            neighbors.append(tuple(new_state))
            
    return neighbors

def dfs(start_state, goal_state):
    stack = [(start_state, [start_state])]
    visited = set()

    print("Starting DFS...")
    nodes_explored = 0

    while stack:
        current_state, path = stack.pop()
        nodes_explored += 1

        if current_state == goal_state:
            print(f"DFS Solution found! Nodes explored: {nodes_explored}, Path length: {len(path)-1}")
            return path

        if current_state not in visited:
            visited.add(current_state)
            # Add neighbors to the stack
            for neighbor in get_neighbors(current_state):
                if neighbor not in visited:
                    stack.append((neighbor, path + [neighbor]))

    print("DFS failed to find a solution.")
    return None


def dls(current_state, goal_state, limit, path, visited):
    """Depth-Limited Search (Helper for IDS)"""
    if current_state == goal_state:
        return path
    
    if limit <= 0:
        return "CUTOFF"
    
    cutoff_occurred = False
    
    for neighbor in get_neighbors(current_state):
        # Cycle checking within the current path
        if neighbor not in visited:
            visited.add(neighbor)
            result = dls(neighbor, goal_state, limit - 1, path + [neighbor], visited)
            
            if result == "CUTOFF":
                cutoff_occurred = True
            elif result is not None:
                return result
                
            visited.remove(neighbor) # Backtrack

    return "CUTOFF" if cutoff_occurred else None

def ids(start_state, goal_state, max_depth=50):
    print(f"Starting IDS (max depth = {max_depth})...")
    
    for depth in range(max_depth):
        visited = set([start_state])
        result = dls(start_state, goal_state, depth, [start_state], visited)
        
        if result != "CUTOFF" and result is not None:
            print(f"IDS Solution found at depth: {depth}")
            return result
            
    print("IDS failed to find a solution within the maximum depth limit.")
    return None

if __name__ == "__main__":
    print("Initial State:")
    print_state(INITIAL_STATE)
    print("Goal State:")
    print_state(GOAL_STATE)
    
    ids_path = ids(INITIAL_STATE, GOAL_STATE)
    if ids_path:
        print("\nLast 3 steps of IDS solution:")
        for step in ids_path[-3:]:
            print_state(step)

    print("-" * 40)
    
  
    dfs_path = dfs(INITIAL_STATE, GOAL_STATE)
    if dfs_path:
        print(f"\nDFS found a path of length {len(dfs_path)-1}.")
        # Only printing the last 3 steps to avoid flooding the console
        print("Last 3 steps of DFS solution:")
        for step in dfs_path[-3:]:
            print_state(step)
