import random

pixels = [25, 30, 28, 32, 29, 120, 125, 130, 122, 128, 215, 220, 225, 218, 222]
mean_all = sum(pixels) / len(pixels)
N, pa, T = 10, 0.25, 40

def fitness(t):
    t1, t2 = sorted(t)
    groups = [
        [p for p in pixels if p <= t1],
        [p for p in pixels if t1 < p <= t2],
        [p for p in pixels if p > t2]
    ]
    if any(len(g) == 0 for g in groups):
        return 0
    return sum((len(g) / len(pixels)) * ((sum(g) / len(g) - mean_all) ** 2) for g in groups)

nests = [sorted(random.sample(range(1, 255), 2)) for _ in range(N)]
best = max(nests, key=fitness)

for _ in range(T):
    for i in range(N):
        step = random.gauss(0, 1) / ((abs(random.gauss(0, 1)) + 1e-6) ** (1 / 1.5))
        cand = sorted([max(1, min(254, round(nests[i][d] + 5 * step))) for d in range(2)])
        j = random.randrange(N)
        if fitness(cand) > fitness(nests[j]):
            nests[j] = cand
    nests.sort(key=fitness)
    for i in range(int(pa * N)):
        a, b = random.sample(range(N), 2)
        nests[i] = sorted([max(1, min(254, round(nests[i][d] + random.random() * (nests[a][d] - nests[b][d])))) for d in range(2)])
    best = max(nests + [best], key=fitness)

t1, t2 = best
segmented = [0 if p <= t1 else (1 if p <= t2 else 2) for p in pixels]
print(f"Optimal Thresholds (t1, t2): {t1}, {t2}")
print(f"Max Between-Class Variance:  {fitness(best):.2f}")
print("Segmented Image Labels:     ", segmented)
