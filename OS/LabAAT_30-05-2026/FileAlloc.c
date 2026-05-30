#include <stdio.h>

int disk[50] = {0};

void sequential() {
    int st, len, i, flag = 0;
    printf("\nEnter start block and length: ");
    scanf("%d %d", &st, &len);
    
    for (i = st; i < st + len; i++) {
        if (disk[i] == 1) { flag = 1; break; }
    }
    
    if (flag == 1) {
        printf("Block already allocated. Cannot allocate contiguously.\n");
    } else {
        printf("Sequential Allocation: ");
        for (i = st; i < st + len; i++) {
            disk[i] = 1;
            printf("%d ", i);
        }
        printf("\n");
    }
}

void indexed() {
    int ind, len, i, blocks[20], flag = 0;
    printf("\nEnter index block: ");
    scanf("%d", &ind);
    
    if (disk[ind] == 1) {
        printf("Index block is already allocated.\n");
        return;
    }
    
    printf("Enter file length: ");
    scanf("%d", &len);
    printf("Enter %d blocks: ", len);
    for (i = 0; i < len; i++) {
        scanf("%d", &blocks[i]);
        if (disk[blocks[i]] == 1) flag = 1;
    }
    
    if (flag == 1) {
        printf("One or more data blocks are already allocated.\n");
    } else {
        disk[ind] = 1;
        printf("Indexed Allocation -> Index Block %d: ", ind);
        for (i = 0; i < len; i++) {
            disk[blocks[i]] = 1;
            printf("%d ", blocks[i]);
        }
        printf("\n");
    }
}

void linked() {
    int st, len, i, count = 0;
    printf("\nEnter start block and length: ");
    scanf("%d %d", &st, &len);
    
    if (disk[st] == 1) {
        printf("Start block is already allocated.\n");
        return;
    }
    
    disk[st] = 1;
    printf("Linked Allocation: %d ", st);
    count++;
    
    for (i = st + 1; i < 50 && count < len; i++) {
        if (disk[i] == 0) {
            disk[i] = 1;
            printf("-> %d ", i);
            count++;
        }
    }
    
    if (count == len) printf("\n");
    else printf("\nNot enough free blocks available.\n");
}

int main() {
    int ch;
    while (1) {
        printf("\n--- File Allocation Strategies ---\n");
        printf("1. Sequential  2. Indexed  3. Linked  4. Exit\n");
        printf("Enter your choice: ");
        scanf("%d", &ch);
        
        switch (ch) {
            case 1: sequential(); break;
            case 2: indexed(); break;
            case 3: linked(); break;
            case 4: return 0;
            default: printf("Invalid choice!\n");
        }
    }
    return 0;
}
