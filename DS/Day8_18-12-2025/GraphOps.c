#include <stdio.h>

int a[20][20], visited[20], n;

void bfs(int v) {
    int q[20], f = 0, r = 0;
    q[r++] = v;
    visited[v] = 1;
    printf("BFS: ");
    while (f < r) {
        int curr = q[f++];
        printf("%d ", curr);
        for (int i = 0; i < n; i++) {
            if (a[curr][i] && !visited[i]) {
                q[r++] = i;
                visited[i] = 1;
            }
        }
    }
    printf("\n");
}

void dfs(int v) {
    visited[v] = 1;
    for (int i = 0; i < n; i++) {
        if (a[v][i] && !visited[i]) {
            dfs(i);
        }
    }
}

int main() {
    printf("Enter number of vertices: ");
    scanf("%d", &n);
    printf("Enter adjacency matrix:\n");
    for (int i = 0; i < n; i++)
        for (int j = 0; j < n; j++)
            scanf("%d", &a[i][j]);

    // BFS Part
    for (int i = 0; i < n; i++) visited[i] = 0;
    bfs(0);

    // DFS Connectivity Part
    for (int i = 0; i < n; i++) visited[i] = 0;
    dfs(0);

    int connected = 1;
    for (int i = 0; i < n; i++) {
        if (!visited[i]) connected = 0;
    }

    if (connected) printf("Graph is Connected.\n");
    else printf("Graph is NOT Connected.\n");

    return 0;
}
