#include <stdio.h>

int main() {
    int n, i, j, p[10], d[10], b[10], time = 0;

    printf("Enter number of processes: ");
    scanf("%d", &n);

    for (i = 0; i < n; i++) {
        p[i] = i + 1;
        printf("P%d (BT and Deadline): ", p[i]);
        scanf("%d %d", &b[i], &d[i]);
    }

    for (i = 0; i < n - 1; i++) {
        for (j = i + 1; j < n; j++) {
            if (d[i] > d[j]) {
                int t = d[i]; d[i] = d[j]; d[j] = t;
                t = b[i]; b[i] = b[j]; b[j] = t;
                t = p[i]; p[i] = p[j]; p[j] = t;
            }
        }
    }

    printf("\nGantt Chart:\n|");
    for (i = 0; i < n; i++) printf(" P%d |", p[i]);
    printf("\n0");
    for (i = 0; i < n; i++) {
        time += b[i];
        printf("   %d", time);
    }
    printf("\n");

    return 0;
}
/* Output:
Enter number of processes: 3
P1 (BT and Deadline): 2 10
P2 (BT and Deadline): 3 5
P3 (BT and Deadline): 1 7

Gantt Chart:
| P2 | P3 | P1 |
0   3   4   6
*/