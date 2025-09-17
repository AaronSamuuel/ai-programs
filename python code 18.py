import numpy as np

def tsp(cities):
    # Create a distance matrix
    n = len(cities)
    dist_matrix = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            if i != j:
                dist_matrix[i][j] = np.linalg.norm(cities[i] - cities[j])

    # Initialize variables
    tour = [0]
    unvisited_cities = set(range(1, n))
    total_distance = 0

    # Find the nearest unvisited city and add it to the tour
    while unvisited_cities:
        current_city = tour[-1]
        nearest_city = min(unvisited_cities, key=lambda city: dist_matrix[current_city][city])
        tour.append(nearest_city)
        unvisited_cities.remove(nearest_city)
        total_distance += dist_matrix[current_city][nearest_city]

    # Complete the tour by returning to the starting city
    tour.append(0)
    total_distance += dist_matrix[tour[-2]][0]

    return tour, total_distance


# Example usage
if __name__ == "__main__":
    # Define cities as numpy arrays (x, y coordinates)
    cities = np.array([
        [0, 0],
        [1, 5],
        [5, 2],
        [6, 6]
    ])

    tour, distance = tsp(cities)
    print("Tour:", tour)
    print("Total distance:", distance)
