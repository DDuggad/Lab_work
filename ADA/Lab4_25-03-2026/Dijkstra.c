#include <stdio.h>
#define INF 999

void dijkstra(int n, int cost[10][10], int src) {
    int dist[10], vis[10] = {0}, i, j, u, min;

    for (i = 1; i <= n; i++) dist[i] = cost[src][i];
    dist[src] = 0;
    vis[src] = 1;

    for (i = 1; i < n; i++) {
        min = INF;
        u = -1;
        for (j = 1; j <= n; j++) {
            if (!vis[j] && dist[j] < min) {
                min = dist[j];
                u = j;
            }
        }
        if (u == -1) break;
        vis[u] = 1;
        for (j = 1; j <= n; j++) {
            if (!vis[j] && (dist[u] + cost[u][j] < dist[j]))
                dist[j] = dist[u] + cost[u][j];
        }
    }

    printf("\nNode\tDistance from %d\n", src);
    for (i = 1; i <= n; i++) {
        if (dist[i] >= INF) printf("%d\tINF\n", i);
        else printf("%d\t%d\n", i, dist[i]);
    }
}

int main() {
    int n, i, j, src, cost[10][10];
    printf("Enter n: "); scanf("%d", &n);
    printf("Enter Matrix (%d for INF):\n", INF);
    for (i = 1; i <= n; i++)
        for (j = 1; j <= n; j++)
            scanf("%d", &cost[i][j]);
    printf("Enter Source: "); scanf("%d", &src);
    dijkstra(n, cost, src);
    return 0;
}
