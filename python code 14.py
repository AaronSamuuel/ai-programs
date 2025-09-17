from typing import List, Tuple
from collections import deque

def is_valid_state(state: Tuple[int, int, int, int, int]) -> bool:
    """Check if a state is valid."""
    m1, c1, m2, c2, boat = state
    if m1 < 0 or c1 < 0 or m2 < 0 or c2 < 0:
        return False
    if (m1 > 0 and m1 < c1) or (m2 > 0 and m2 < c2):
        return False
    return True

def get_successors(state: Tuple[int, int, int, int, int]) -> List[Tuple[int, int, int, int, int]]:
    """Generate all valid successor states."""
    m1, c1, m2, c2, boat = state
    successors = []

    # Boat on left side
    if boat == 1:
        for i in range(3):
            for j in range(3):
                if i + j >= 1 and i + j <= 2:  # 1 or 2 passengers
                    new_state = (m1 - i, c1 - j, m2 + i, c2 + j, 0)
                    if is_valid_state(new_state):
                        successors.append(new_state)

    # Boat on right side
    else:
        for i in range(3):
            for j in range(3):
                if i + j >= 1 and i + j <= 2:
                    new_state = (m1 + i, c1 + j, m2 - i, c2 - j, 1)
                    if is_valid_state(new_state):
                        successors.append(new_state)

    return successors

def breadth_first_search() -> List[Tuple[int, int, int, int, int]]:
    """Find solution using BFS."""
    initial_state = (3, 3, 0, 0, 1)  # (m1, c1, m2, c2, boat=1 left)
    goal_state = (0, 0, 3, 3, 0)     # all moved to right side
    visited = set()
    queue = deque([(initial_state, [])])

    while queue:
        state, path = queue.popleft()
        if state == goal_state:
            return path + [state]
        visited.add(state)
        for successor in get_successors(state):
            if successor not in visited:
                queue.append((successor, path + [state]))

    return []

if __name__ == '__main__':
    solution = breadth_first_search()
    print("Solution Path:")
    for step, state in enumerate(solution):
        print(f"Step {step}: {state}")
