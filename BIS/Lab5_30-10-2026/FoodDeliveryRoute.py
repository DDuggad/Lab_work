import random, math

stops = [(0, 0), (2, 6), (5, 2), (7, 7), (4, 1)]
names = ["Restaurant", "Stop A", "Stop B", "Stop C", "Stop D"]
N, M, T = len(stops), 6, 30
alpha, beta, rho = 1, 2, 0.5
pher = [[1.0] * N for _ in range(N)]
best_tour, best_dist = None, float("inf")

for _ in range(T):
    tours = []
    for _ in range(M):
        tour = [0]
        while len(tour) < N:
            curr = tour[-1]
            unvisited = [j for j in range(N) if j not in tour]
            weights = [(pher[curr][j] ** alpha) * ((1 / math.dist(stops[curr], stops[j])) ** beta) for j in unvisited]
            tour.append(random.choices(unvisited, weights=weights)[0])
        dist = sum(math.dist(stops[tour[i]], stops[tour[(i + 1) % N]]) for i in range(N))
        tours.append((tour, dist))
        if dist < best_dist:
            best_tour, best_dist = tour, dist
    for i in range(N):
        for j in range(N):
            pher[i][j] *= (1 - rho)
    for tour, dist in tours:
        for i in range(N):
            u, v = tour[i], tour[(i + 1) % N]
            pher[u][v] += 1 / dist
            pher[v][u] += 1 / dist

route = " -> ".join(names[i] for i in best_tour + [0])
print("Best Delivery Route:", route)
print(f"Minimum Distance:    {best_dist:.2f} km")
