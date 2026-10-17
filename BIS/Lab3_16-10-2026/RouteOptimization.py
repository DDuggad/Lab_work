import random, math

# 1) Start & Inputs
P, Cr, Mr, G = 20, 0.8, 0.2, 100

# Cities as (x, y) coordinates
cities = [(0, 0), (1, 5), (5, 2), (6, 6), (8, 3), (3, 7), (7, 1)]
S = len(cities)

# 2) Objective Function (Total route distance) & Fitness (1 / distance)
def route_distance(route):
    return sum(math.dist(cities[route[i]], cities[route[(i + 1) % S]]) for i in range(S))

def fitness(route):
    return 1 / route_distance(route)  # Smaller distance = Higher fitness

# 3) Initialize random population of P chromosomes of length S
pop = [random.sample(range(S), S) for _ in range(P)]

# 4 & 5) Evaluate fitness & store the best chromosome found so far
best = max(pop, key=fitness)

# 6) Repeat for G Generations
for _ in range(G):
    # (v) Elitism: start next population with the best chromosome so far
    next_pop = [best[:]]

    while len(next_pop) < P:
        # (i) Tournament Selection (pick 3 random, best wins)
        p1 = max(random.sample(pop, 3), key=fitness)
        p2 = max(random.sample(pop, 3), key=fitness)

        # (ii) Ordered One-Point Crossover with probability Cr
        if random.random() < Cr:
            cut = random.randint(1, S - 1)
            head = p1[:cut]
            child = head + [city for city in p2 if city not in head]
        else:
            child = p1[:]

        # (iii) Swap Mutation with probability Mr
        if random.random() < Mr:
            i, j = random.sample(range(S), 2)
            child[i], child[j] = child[j], child[i]

        next_pop.append(child)

    # (iv & vi) Update population and best solution found so far
    pop = next_pop
    current_best = max(pop, key=fitness)
    if fitness(current_best) > fitness(best):
        best = current_best[:]

# 7, 8 & 9) Display Best Route, Distance & Fitness, then Stop
print(f"Best Route:    {best} -> {best[0]}")
print(f"Min Distance:  {route_distance(best):.2f}")
print(f"Fitness Value: {fitness(best):.4f}")
