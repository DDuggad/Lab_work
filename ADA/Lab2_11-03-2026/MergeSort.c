#include <stdio.h>
#include <stdlib.h>
#include <time.h>

void merge(int a[], int low, int mid, int high) {
    int i = low, j = mid + 1, k = 0;
    int *b = (int*)malloc((high - low + 1) * sizeof(int));

    while (i <= mid && j <= high) {
        if (a[i] < a[j]) b[k++] = a[i++];
        else b[k++] = a[j++];
    }
    while (i <= mid) b[k++] = a[i++];
    while (j <= high) b[k++] = a[j++];

    for (i = low, k = 0; i <= high; i++, k++) a[i] = b[k];
    free(b);
}

void mergeSort(int a[], int low, int high) {
    if (low < high) {
        int mid = (low + high) / 2;
        mergeSort(a, low, mid);
        mergeSort(a, mid + 1, high);
        merge(a, low, mid, high);
    }
}

int main() {
    int n, i;
    clock_t start, end;

    printf("Enter number of elements (N): ");
    scanf("%d", &n);

    int *a = (int*)malloc(n * sizeof(int));
    
    // Generate random numbers
    for (i = 0; i < n; i++) a[i] = rand() % 10000;

    start = clock();
    mergeSort(a, 0, n - 1);
    end = clock();

    double time_taken = ((double)(end - start)) / CLOCKS_PER_SEC;

    printf("Sorted first 5 elements: ");
    for(i=0; i<5 && i<n; i++) printf("%d ", a[i]);
    
    printf("\nTime taken for N=%d: %f seconds\n", n, time_taken);

    free(a);
    return 0;
}
