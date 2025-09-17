from collections import deque

def water_jug_problem(x, y, z):
    """
    Solves the water jug problem using breadth-first search.
    x: size of jug 1
    y: size of jug 2
    z: target amount of water
    Returns the sequence of steps to reach the target amount of water.
    """
    queue = deque([(0, 0, [])])  # Start with both jugs empty
    visited = set()

    while queue:
        a, b, steps = queue.popleft()

        if (a, b) in visited:
            continue
        visited.add((a, b))

        # Check if solution found
        if a == z or b == z:
            return steps

        # Fill jug 1
        queue.append((x, b, steps + ['Fill jug 1']))
        # Fill jug 2
        queue.append((a, y, steps + ['Fill jug 2']))
        # Empty jug 1
        queue.append((0, b, steps + ['Empty jug 1']))
        # Empty jug 2
        queue.append((a, 0, steps + ['Empty jug 2']))
        # Pour jug 1 into jug 2
        amount = min(a, y - b)
        queue.append((a - amount, b + amount, steps + ['Pour jug 1 into jug 2']))
        # Pour jug 2 into jug 1
        amount = min(x - a, b)
        queue.append((a + amount, b - amount, steps + ['Pour jug 2 into jug 1']))

    return None


# Example: jug1 = 4 liters, jug2 = 3 liters, target = 2 liters
steps = water_jug_problem(4, 3, 2)

if steps:
    print("Steps to solve the problem:")
    print('\n'.join(steps))
else:
    print('No solution found.')
