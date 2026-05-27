
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

void heapify(int a[], int n, int i) {
    int largest = i;
    int left = 2 * i + 1;
    int right = 2 * i + 2;

    if (left < n && a[left] > a[largest]) largest = left;
    if (right < n && a[right] > a[largest]) largest = right;

    if (largest != i) {
        int t = a[i]; a[i] = a[largest]; a[largest] = t;
        heapify(a, n, largest);
    }
}

void heapSort(int a[], int n) {
    for (int i = n / 2 - 1; i >= 0; i--)
        heapify(a, n, i);

    for (int i = n - 1; i >= 0; i--) {
        int t = a[0]; a[0] = a[i]; a[i] = t;
        heapify(a, i, 0);
    }
}

int main() {
    int n, i;
    clock_t start, end;

    printf("Enter number of elements (N): ");
    scanf("%d", &n);

    int *a = (int*)malloc(n * sizeof(int));
    for (i = 0; i < n; i++) a[i] = rand() % 10000;

    start = clock();
    heapSort(a, n);
    end = clock();

    double t = ((double)(end - start)) / CLOCKS_PER_SEC;

    printf("Sorted first 5 elements: ");
    for (i = 0; i < 5 && i < n; i++) printf("%d ", a[i]);
    printf("\nTime taken for N=%d: %f seconds\n", n, t);

    free(a);
    return 0;
}