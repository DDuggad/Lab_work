#include <stdio.h>

int main() {
    int n, m, i, j, k, alloc[10][10], req[10][10], avail[10], f[10];

    printf("Enter no. of processes and resources: ");
    scanf("%d %d", &n, &m);

    printf("Enter Allocation Matrix:\n");
    for (i = 0; i < n; i++) for (j = 0; j < m; j++) scanf("%d", &alloc[i][j]);

    printf("Enter Request Matrix:\n");
    for (i = 0; i < n; i++) for (j = 0; j < m; j++) scanf("%d", &req[i][j]);

    printf("Enter Available Resources: ");
    for (i = 0; i < m; i++) scanf("%d", &avail[i]);

    for (i = 0; i < n; i++) {
        int sum = 0;
        for (j = 0; j < m; j++) sum += alloc[i][j];
        f[i] = (sum == 0) ? 1 : 0;
    }

    for (k = 0; k < n; k++) {
        for (i = 0; i < n; i++) {
            if (f[i] == 0) {
                int can_exec = 1;
                for (j = 0; j < m; j++) {
                    if (req[i][j] > avail[j]) { can_exec = 0; break; }
                }
                if (can_exec) {
                    for (j = 0; j < m; j++) avail[j] += alloc[i][j];
                    f[i] = 1;
                }
            }
        }
    }

    int deadlocked = 0;
    for (i = 0; i < n; i++) {
        if (f[i] == 0) {
            if (!deadlocked) printf("\nDeadlock detected at: ");
            printf("P%d ", i);
            deadlocked = 1;
        }
    }

    if (!deadlocked) printf("\nNo Deadlock Detected.\n");
    return 0;
}
/* Output:
Enter no. of processes and resources: 3 3
Enter Allocation Matrix: 0 1 0  2 0 0  3 0 3
Enter Request Matrix: 0 0 0  2 0 2  0 0 0
Enter Available Resources: 0 0 0

No Deadlock Detected.
*/