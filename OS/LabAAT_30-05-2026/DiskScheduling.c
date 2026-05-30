#include <stdio.h>
#include <stdlib.h>

void sort(int a[], int n) {
    int i, j, t;
    for (i = 0; i < n - 1; i++) {
        for (j = i + 1; j < n; j++) {
            if (a[i] > a[j]) { t = a[i]; a[i] = a[j]; a[j] = t; }
        }
    }
}

void fcfs(int p[], int n, int head) {
    int i, tot = 0, curr = head;
    printf("\nFCFS Sequence: ");
    for (i = 0; i < n; i++) {
        printf("%d ", p[i]);
        tot += abs(curr - p[i]);
        curr = p[i];
    }
    printf("\nTotal Head Movement: %d\n", tot);
}

void sstf(int p[], int n, int head) {
    int i, j, tot = 0, curr = head, vis[20] = {0};
    printf("\nSSTF Sequence: ");
    for (i = 0; i < n; i++) {
        int min = 9999, idx = -1;
        for (j = 0; j < n; j++) {
            if (!vis[j] && abs(curr - p[j]) < min) {
                min = abs(curr - p[j]);
                idx = j;
            }
        }
        vis[idx] = 1;
        printf("%d ", p[idx]);
        tot += min;
        curr = p[idx];
    }
    printf("\nTotal Head Movement: %d\n", tot);
}

void scan(int p[], int n, int head, int m) {
    int i, a[20], tot = 0, pos = 0, curr = head;
    for (i = 0; i < n; i++) a[i] = p[i];
    sort(a, n);
    while (pos < n && a[pos] < head) pos++;

    printf("\nSCAN Sequence: ");
    for (i = pos; i < n; i++) {
        printf("%d ", a[i]);
        tot += abs(curr - a[i]);
        curr = a[i];
    }
    if (pos > 0) {
        tot += abs(curr - m);
        curr = m;
        for (i = pos - 1; i >= 0; i--) {
            printf("%d ", a[i]);
            tot += abs(curr - a[i]);
            curr = a[i];
        }
    }
    printf("\nTotal Head Movement: %d\n", tot);
}

void clook(int p[], int n, int head) {
    int i, a[20], tot = 0, pos = 0, curr = head;
    for (i = 0; i < n; i++) a[i] = p[i];
    sort(a, n);
    while (pos < n && a[pos] < head) pos++;

    printf("\nC-LOOK Sequence: ");
    for (i = pos; i < n; i++) {
        printf("%d ", a[i]);
        tot += abs(curr - a[i]);
        curr = a[i];
    }
    for (i = 0; i < pos; i++) {
        printf("%d ", a[i]);
        tot += abs(curr - a[i]);
        curr = a[i];
    }
    printf("\nTotal Head Movement: %d\n", tot);
}

int main() {
    int p[20], n, head, m, i, ch;

    printf("Enter maximum track limit (e.g., 199 for 0-199): "); scanf("%d", &m);
    printf("Enter initial head position: "); scanf("%d", &head);
    printf("Enter number of requests: "); scanf("%d", &n);
    printf("Enter the requests: ");
    for (i = 0; i < n; i++) scanf("%d", &p[i]);

    while (1) {
        printf("\n--- Disk Scheduling Algorithms ---\n");
        printf("1. FCFS  2. SSTF  3. SCAN  4. C-LOOK  5. Exit\n");
        printf("Enter choice: ");
        scanf("%d", &ch);

        switch (ch) {
            case 1: fcfs(p, n, head); break;
            case 2: sstf(p, n, head); break;
            case 3: scan(p, n, head, m); break;
            case 4: clook(p, n, head); break;
            case 5: return 0;
            default: printf("Invalid choice!\n");
        }
    }
    return 0;
}
