from typing import List, Tuple

def get_successors(state: Tuple[Tuple[int, int], List[List[int]]]) -> List[Tuple[Tuple[int, int], List[List[int]]]]:
    """Generate all possible valid states that can be reached from a given state."""
    position, grid = state
    successors = []
    for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        x, y = position
        new_x, new_y = x + dx, y + dy
        if 0 <= new_x < len(grid) and 0 <= new_y < len(grid[0]):
            new_grid = [row[:] for row in grid]  # deep copy
            if new_grid[new_x][new_y] == 1:      # clean dirt
                new_grid[new_x][new_y] = 0
            successors.append(((new_x, new_y), new_grid))
    return successors

def make_hashable(state: Tuple[Tuple[int, int], List[List[int]]]):
    """Convert state to a hashable form for visited set."""
    position, grid = state
    grid_tuple = tuple(tuple(row) for row in grid)
    return (position, grid_tuple)

def depth_first_search(state: Tuple[Tuple[int, int], List[List[int]]], visited: set) -> bool:
    """Find the solution using a depth-first search algorithm."""
    if all(all(cell == 0 for cell in row) for row in state[1]):  # all cleaned
        return True
    
    visited.add(make_hashable(state))
    
    for successor in get_successors(state):
        if make_hashable(successor) not in visited:
            if depth_first_search(successor, visited):
                return True
    return False

if __name__ == '__main__':
    grid = [
        [0, 1, 1, 1],
        [0, 0, 1, 0],
        [1, 0, 0, 1],
        [1, 1, 1, 0]
    ]
    initial_state = ((0, 0), grid)
    if depth_first_search(initial_state, set()):
        print("The room can be cleaned.")
    else:
        print("The room cannot be cleaned.")
