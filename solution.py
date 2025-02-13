from algorithms import hill_climbing, random_local_search, simulated_annealing

def sphere_function(x):
    return sum(xi ** 2 for xi in x)


if __name__ == "__main__":
    bounds = [(-5, 5), (-5, 5)]

    print("Hill Climbing:")
    hc_solution, hc_value = hill_climbing(sphere_function, bounds)

    print("\nRandom Local Search:")
    rls_solution, rls_value = random_local_search(sphere_function, bounds)

    print("\nSimulated Annealing:")
    sa_solution, sa_value = simulated_annealing(sphere_function, bounds, temp=10)

    print("\nHill Climbing Solution:", hc_solution, "Value:", hc_value)
    print("\nRandom Local Search Solution:", rls_solution, "Value:", rls_value)
    print("\nSimulated Annealing Solution:", sa_solution, "Value:", sa_value)