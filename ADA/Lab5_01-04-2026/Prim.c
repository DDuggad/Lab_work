#include <stdio.h>
#define INF 999

void prim(int n, int cost[10][10]) {
    int selected[10] = {0}, i, j, ne = 1;
    int min, a, b, u, v, mincost = 0;

    selected[1] = 1;

    while (ne < n) {
        min = INF;
        for (i = 1; i <= n; i++) {
            for (j = 1; j <= n; j++) {
                if (cost[i][j] < min) {
                    if (selected[i] != 0 && selected[j] == 0) {
                        min = cost[i][j];
                        a = u = i;
                        b = v = j;
                    }
                }
            }
        }

        if (selected[u] == 1 && selected[v] == 0) {
            printf("Edge %d: (%d, %d) cost: %d\n", ne++, a, b, min);
            mincost += min;
            selected[v] = 1;
        }
        cost[a][b] = cost[b][a] = INF;
    }
    printf("Total min cost: %d\n", mincost);
}

int main() {
    int n, i, j, cost[10][10];
    printf("Enter n: "); scanf("%d", &n);
    printf("Enter matrix (%d for INF):\n", INF);
    for (i = 1; i <= n; i++)
        for (j = 1; j <= n; j++)
            scanf("%d", &cost[i][j]);
    prim(n, cost);
    return 0;
}
