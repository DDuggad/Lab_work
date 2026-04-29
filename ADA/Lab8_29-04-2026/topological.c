#include <stdio.h>

void topo(int n, int a[10][10]) {
    int in[10] = {0}, res[10], vis[10] = {0};
    int i, j, k, count = 0;

    // Calculate in-degree of each vertex
    for (i = 1; i <= n; i++)
        for (j = 1; j <= n; j++)
            if (a[i][j] == 1) in[j]++;

    while (count < n) {
        int u = -1;
        // Find a vertex with in-degree 0 that isn't visited
        for (i = 1; i <= n; i++) {
            if (in[i] == 0 && !vis[i]) {
                u = i;
                break;
            }
        }

        if (u == -1) {
            printf("\nCycle detected! Not a DAG.\n");
            return;
        }

        vis[u] = 1;
        res[count++] = u;

        // "Remove" vertex by updating neighbors' in-degrees
        for (v = 1; v <= n; v++) {
            if (a[u][v] == 1) in[v]--;
        }
    }

    printf("\nTopological Order: ");
    for (i = 0; i < n; i++) printf("%d ", res[i]);
    printf("\n");
}

int main() {
    int n, i, j, a[10][10];
    printf("Enter n: "); scanf("%d", &n);
    printf("Enter Adjacency Matrix:\n");
    for (i = 1; i <= n; i++)
        for (j = 1; j <= n; j++)
            scanf("%d", &a[i][j]);

    topo(n, a);
    return 0;
}
