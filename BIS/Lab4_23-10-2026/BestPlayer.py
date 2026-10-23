import random

# 1) Start & Dataset (Name, Goals, Assists, Pass_Accuracy, Tackles)
players = [
    ("Player A", 12, 8,  82, 15),
    ("Player B", 28, 14, 88, 10),
    ("Player C", 5,  18, 91, 22),
    ("Player D", 34, 16, 89, 12),
    ("Player E", 19, 11, 85, 18),
    ("Player F", 9,  6,  79, 30)
]
N = len(players) - 1  # Allowed search bounds: index 0 to 5

# PSO Hyperparameters
S, T = 3, 20              # S = 3 particles (scouts), T = 20 iterations
w, c1, c2 = 0.5, 1.5, 1.5 # Inertia, personal weight, social weight

# 2) Define the objective function f(x) -> Soccer Fitness Score
def f(x):
    idx = round(x) # Convert continuous position x to nearest player index
    _, goals, assists, pass_acc, tackles = players[idx]
    return (goals * 4) + (assists * 3) + (pass_acc * 2) + tackles

# 3) Initialize random positions & velocities for all S particles
pos = [random.uniform(0, N) for _ in range(S)]
vel = [random.uniform(-1, 1) for _ in range(S)]

# 4 & 5) Evaluate fitness & set each particle's personal best (pbest) to initial
pbest = pos[:]

# 6) Set global best (gbest) to the best particle in the swarm
gbest = max(pbest, key=f)

# 7) Repeat for T iterations
for _ in range(T):
    for i in range(S):
        # a) Generate random values r1, r2
        r1, r2 = random.random(), random.random()

        # b) Update velocity using the velocity equation
        vel[i] = w * vel[i] + c1 * r1 * (pbest[i] - pos[i]) + c2 * r2 * (gbest - pos[i])

        # c) Update position using the position equation
        pos[i] = pos[i] + vel[i]

        # d) Keep the particle within the allowed search space [0, N]
        pos[i] = max(0, min(N, pos[i]))

        # e & f) Evaluate fitness of new position; if better than pbest, update pbest
        if f(pos[i]) > f(pbest[i]):
            pbest[i] = pos[i]

        # g) If new position is better than gbest, update gbest
        if f(pos[i]) > f(gbest):
            gbest = pos[i]

# 8 & 9) Display gbest & its fitness value, then Stop
best_idx = round(gbest)
print(f"Best Player Found : {players[best_idx][0]} (Index {best_idx})")
print(f"Fitness Value     : {f(gbest)}")
