#include <stdio.h>

int p[10], d[10], n; // p: elements, d: directions (0 for L, 1 for R)

void print() {
    for (int i = 0; i < n; i++) printf("%d ", p[i]);
    printf("\n");
}

int findMobile() {
    int mob = -1, idx = -1;
    for (int i = 0; i < n; i++) {
        if (d[i] == 0 && i > 0 && p[i] > p[i-1]) {
            if (p[i] > mob) { mob = p[i]; idx = i; }
        }
        if (d[i] == 1 && i < n-1 && p[i] > p[i+1]) {
            if (p[i] > mob) { mob = p[i]; idx = i; }
        }
    }
    return idx;
}

void swap(int i, int j) {
    int t = p[i]; p[i] = p[j]; p[j] = t;
    t = d[i]; d[i] = d[j]; d[j] = t;
}

int main() {
    printf("Enter n: ");
    scanf("%d", &n);

    for (int i = 0; i < n; i++) {
        p[i] = i + 1;
        d[i] = 0;
    }

    print();
    int m_idx;
    while ((m_idx = findMobile()) != -1) {
        int mobile = p[m_idx];
        if (d[m_idx] == 0) swap(m_idx, m_idx - 1);
        else swap(m_idx, m_idx + 1);

        for (int i = 0; i < n; i++) {
            if (p[i] > mobile) d[i] = !d[i];
        }
        print();
    }
    return 0;
}
