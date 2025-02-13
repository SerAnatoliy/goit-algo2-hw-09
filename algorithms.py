import random
import math

def random_local_search(func, bounds, step_size=0.5, probability=0.2, iterations=1000, epsilon=1e-6):
    dim = len(bounds)
    current_point = [random.uniform(b[0], b[1]) for b in bounds]
    current_value = func(current_point)

    for i in range(iterations):
        if i % 10 == 0:
            print("Random Local Search Iteration", i, "Current point:", current_point, "Value:", current_value)

        new_point = []

        for d in range(dim):
            new_coord = current_point[d] + random.uniform(-step_size, step_size)
            new_coord = max(min(new_coord, bounds[d][1]), bounds[d][0])
            new_point.append(new_coord)

        new_value = func(new_point)

        if new_value < current_value or random.random() < probability:
            if abs(current_value - new_value) < epsilon:
                break

            current_point = new_point
            current_value = new_value

    return current_point, current_value

def hill_climbing(func, bounds, iterations=1000, epsilon=1e-6):
    dim = len(bounds)
    current_point = [random.uniform(b[0], b[1]) for b in bounds]
    current_value = func(current_point)
    step_size = 0.1

    for i in range(iterations):
        if i % 10 == 0:
            print("Hill Climbing Iteration", i, "Current point:", current_point, "Value:", current_value)

        neighbors = []

        for d in range(dim):
            new_point_plus = current_point.copy()
            new_point_plus[d] += step_size

            if new_point_plus[d] > bounds[d][1]:
                new_point_plus[d] = bounds[d][1]

            new_point_minus = current_point.copy()
            new_point_minus[d] -= step_size

            if new_point_minus[d] < bounds[d][0]:
                new_point_minus[d] = bounds[d][0]

            neighbors.append(new_point_plus)
            neighbors.append(new_point_minus)

        best_neighbor = current_point
        best_value = current_value

        for neighbor in neighbors:
            value = func(neighbor)
            if value < best_value:
                best_value = value
                best_neighbor = neighbor

        if abs(current_value - best_value) < epsilon:
            break

        current_point = best_neighbor
        current_value = best_value

    return current_point, current_value

def simulated_annealing(func, bounds, iterations=1000, temp=1000, cooling_rate=0.95, epsilon=1e-6):
    dim = len(bounds)
    current_solution = [random.uniform(b[0], b[1]) for b in bounds]
    current_energy = func(current_solution)

    for i in range(iterations):
        if i % 10 == 0:
            print("Simulated Annealing Iteration", i, "Current point:", current_solution, "Energy:", current_energy,
                  "Temperature:", temp)

        if temp < epsilon:
            break

        new_solution = []

        for d in range(dim):
            new_coord = current_solution[d] + random.uniform(-1, 1)
            new_coord = max(min(new_coord, bounds[d][1]), bounds[d][0])
            new_solution.append(new_coord)

        new_energy = func(new_solution)
        delta_energy = new_energy - current_energy

        if delta_energy < 0 or random.random() < math.exp(-delta_energy / temp):
            if abs(current_energy - new_energy) < epsilon:
                current_solution = new_solution
                current_energy = new_energy
                break

            current_solution = new_solution
            current_energy = new_energy

        temp *= cooling_rate

    return current_solution, current_energy