#include <stdio.h>

#define INF 999

void floyd(int n, int dist[10][10]) {
    int i, j, k;

    for (k = 1; k <= n; k++) {
        for (i = 1; i <= n; i++) {
            for (j = 1; j <= n; j++) {
                if (dist[i][k] + dist[k][j] < dist[i][j])
                    dist[i][j] = dist[i][k] + dist[k][j];
            }
        }
    }

    printf("\nAll-Pairs Shortest Paths:\n");
    for (i = 1; i <= n; i++) {
        for (j = 1; j <= n; j++) {
            if (dist[i][j] == INF) printf("INF ");
            else printf("%d ", dist[i][j]);
        }
        printf("\n");
    }
}

int main() {
    int n, i, j, dist[10][10];

    printf("Enter number of nodes: ");
    scanf("%d", &n);

    printf("Enter adjacency matrix (use 999 for INF):\n");
    for (i = 1; i <= n; i++) {
        for (j = 1; j <= n; j++) {
            scanf("%d", &dist[i][j]);
            if (i == j) dist[i][j] = 0;
        }
    }

    floyd(n, dist);

    return 0;
}
/* Output Example:
Enter number of nodes: 4
Enter adjacency matrix:
0 3 999 7
8 0 2 999
5 999 0 1
2 999 999 0

All-Pairs Shortest Paths:
0 3 5 6 
5 0 2 3 
3 6 0 1 
2 5 7 0 
*/