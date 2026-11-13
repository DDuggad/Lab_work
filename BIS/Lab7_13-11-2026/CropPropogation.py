import random

N, T = 12, 40
wolves = [[random.uniform(0, 5) for _ in range(3)] for _ in range(N)]

def fitness(w):
    rice, maize, soy = w
    if maize + soy > 5:
        scale = 5 / (maize + soy)
        maize, soy = maize * scale, soy * scale
    return (40 * rice) + (52 * maize) + (48 * soy) + (15 * min(maize, soy))

for t in range(T):
    wolves.sort(key=fitness, reverse=True)
    alpha, beta, delta = wolves[0][:], wolves[1][:], wolves[2][:]
    a = 2 - t * (2 / T)
    for i in range(N):
        new_w = []
        for d in range(3):
            r1, r2 = random.random(), random.random()
            A1, C1 = 2 * a * r1 - a, 2 * r2
            X1 = alpha[d] - A1 * abs(C1 * alpha[d] - wolves[i][d])

            r1, r2 = random.random(), random.random()
            A2, C2 = 2 * a * r1 - a, 2 * r2
            X2 = beta[d] - A2 * abs(C2 * beta[d] - wolves[i][d])

            r1, r2 = random.random(), random.random()
            A3, C3 = 2 * a * r1 - a, 2 * r2
            X3 = delta[d] - A3 * abs(C3 * delta[d] - wolves[i][d])

            new_w.append(max(0, min(5, (X1 + X2 + X3) / 3)))
        if new_w[1] + new_w[2] > 5:
            s = 5 / (new_w[1] + new_w[2])
            new_w[1], new_w[2] = new_w[1] * s, new_w[2] * s
        wolves[i] = new_w

wolves.sort(key=fitness, reverse=True)
rice, maize, soy = wolves[0]
print("Neighbour Land (10 acres Rice):           400.00")
print(f"Your Half 1 (Seasonal Trend - Rice):      {rice:.2f} acres")
print(f"Your Half 2 (Same-Season - Maize, Soy):   {maize:.2f}, {soy:.2f} acres")
print(f"Your Total Land Return (Fitness):         {fitness(wolves[0]):.2f}")
