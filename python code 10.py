from queue import PriorityQueue

goal_state = (1, 2, 3, 4, 5, 6, 7, 8, 0)

# Manhattan distance heuristic
def heuristic(state):
    distance = 0
    for i in range(3):
        for j in range(3):
            tile = state[i * 3 + j]
            if tile != 0:
                x, y = (tile - 1) // 3, (tile - 1) % 3
                distance += abs(x - i) + abs(y - j)
    return distance

def solve(initial_state):
    frontier = PriorityQueue()
    frontier.put((heuristic(initial_state), initial_state))
    explored = set()

    while not frontier.empty():
        _, state = frontier.get()

        if state == goal_state:
            return True

        explored.add(state)

        for successor in successors(state):
            if successor not in explored:
                priority = heuristic(successor) + len(explored)
                frontier.put((priority, successor))

    return False

def successors(state):
    successors = []
    i = state.index(0)

    if i % 3 != 0:
        # Slide tile left
        new_state = list(state)
        new_state[i], new_state[i - 1] = new_state[i - 1], new_state[i]
        successors.append(tuple(new_state))

    if i % 3 != 2:
        # Slide tile right
        new_state = list(state)
        new_state[i], new_state[i + 1] = new_state[i + 1], new_state[i]
        successors.append(tuple(new_state))

    if i // 3 != 0:
        # Slide tile up
        new_state = list(state)
        new_state[i], new_state[i - 3] = new_state[i - 3], new_state[i]
        successors.append(tuple(new_state))

    if i // 3 != 2:
        # Slide tile down
        new_state = list(state)
        new_state[i], new_state[i + 3] = new_state[i + 3], new_state[i]
        successors.append(tuple(new_state))

    return successors

# Example initial state
initial_state = (2, 8, 3,
                 1, 6, 4,
                 7, 0, 5)

if solve(initial_state):
    print("The puzzle is solvable!")
else:
    print("The puzzle is unsolvable.")
