#include <stdio.h>

#define MAX 10

int main() {
    int ht[MAX] = {0}, n, key, index, count = 0;

    printf("Enter number of records: ");
    scanf("%d", &n);

    printf("Enter %d keys (4-digit): ", n);
    for (int i = 0; i < n; i++) {
        if (count == MAX) {
            printf("\nTable Full. Cannot insert.\n");
            break;
        }

        scanf("%d", &key);
        index = key % MAX;

        while (ht[index] != 0) {
            index = (index + 1) % MAX; // Linear Probing
        }

        ht[index] = key;
        count++;
    }

    printf("\nHash Table:\n");
    printf("Index\tKey\n");
    for (int i = 0; i < MAX; i++) {
        if (ht[i] != 0)
            printf("%d\t%d\n", i, ht[i]);
        else
            printf("%d\t-\n", i);
    }
    return 0;
}
