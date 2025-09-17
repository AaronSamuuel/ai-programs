import heapq

def astar(start, goal, neighbors_fn, heuristic_fn):
 
    frontier = []
    heapq.heappush(frontier, (0, start))
    came_from = {start: None}
    cost_so_far = {start: 0}

    while frontier:
        _, current = heapq.heappop(frontier)

        if current == goal:
            break

        for neighbor in neighbors_fn(current):
            new_cost = cost_so_far[current] + 1  # assuming each step cost = 1
            if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                cost_so_far[neighbor] = new_cost
                priority = new_cost + heuristic_fn(neighbor, goal)
                heapq.heappush(frontier, (priority, neighbor))
                came_from[neighbor] = current

    # Reconstruct path
    path = [goal]
    current = goal
    while current != start:
        current = came_from[current]
        path.append(current)
    path.reverse()

    return path, cost_so_far[goal]


# -------------------------
# Example Usage
# -------------------------
def neighbors(node):
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E', 'G'],
        'G': ['F']
    }
    return graph.get(node, [])

def heuristic(node, goal):
    # Simple heuristic: difference in ASCII codes (for demo)
    return abs(ord(goal) - ord(node))

# Run A*
start_node = 'A'
goal_node = 'G'
path, cost = astar(start_node, goal_node, neighbors, heuristic)

print("Shortest Path:", path)
print("Path Cost:", cost)
