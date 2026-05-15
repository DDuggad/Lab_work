#include <stdio.h>

int main() {
    int n, m, i, j, k, alloc[10][10], max[10][10], avail[10], need[10][10], f[10], ans[10], ind = 0;

    printf("Enter no. of processes and resources: ");
    scanf("%d %d", &n, &m);

    printf("Enter Allocation Matrix:\n");
    for (i = 0; i < n; i++) for (j = 0; j < m; j++) scanf("%d", &alloc[i][j]);

    printf("Enter Max Matrix:\n");
    for (i = 0; i < n; i++) for (j = 0; j < m; j++) scanf("%d", &max[i][j]);

    printf("Enter Available Resources: ");
    for (i = 0; i < m; i++) scanf("%d", &avail[i]);

    for (i = 0; i < n; i++) {
        for (j = 0; j < m; j++) need[i][j] = max[i][j] - alloc[i][j];
        f[i] = 0;
    }

    for (k = 0; k < n; k++) {
        for (i = 0; i < n; i++) {
            if (f[i] == 0) {
                int flag = 0;
                for (j = 0; j < m; j++) {
                    if (need[i][j] > avail[j]) { flag = 1; break; }
                }
                if (flag == 0) {
                    ans[ind++] = i;
                    for (int y = 0; y < m; y++) avail[y] += alloc[i][y];
                    f[i] = 1;
                }
            }
        }
    }

    if (ind == n) {
        printf("\nSafe Sequence: ");
        for (i = 0; i < n - 1; i++) printf("P%d -> ", ans[i]);
        printf("P%d\n", ans[n - 1]);
    } else printf("\nSystem is in Unsafe State!\n");

    return 0;
}
/* Output:
Enter no. of processes and resources: 3 3
Enter Allocation Matrix: 0 1 0  2 0 0  3 0 2
Enter Max Matrix: 7 5 3  3 2 2  9 0 2
Enter Available Resources: 3 3 2

Safe Sequence: P1 -> P0 -> P2
*/