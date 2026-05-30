#include <stdio.h>

void single_level() {
    int n, i;
    char files[10][20];
    printf("\nEnter number of files: "); scanf("%d", &n);
    for (i = 0; i < n; i++) {
        printf("Enter file %d name: ", i + 1);
        scanf("%s", files[i]);
    }
    printf("\nDirectory: root\nFiles: ");
    for (i = 0; i < n; i++) printf("%s ", files[i]);
    printf("\n");
}

void two_level() {
    int d, i, j;
    struct { char dname[20]; char fname[10][20]; int fcnt; } dirs[10];
    
    printf("\nEnter number of user directories: "); scanf("%d", &d);
    for (i = 0; i < d; i++) {
        printf("Enter Dir %d name: ", i + 1); scanf("%s", dirs[i].dname);
        printf("Number of files in %s: ", dirs[i].dname); scanf("%d", &dirs[i].fcnt);
        for (j = 0; j < dirs[i].fcnt; j++) {
            printf("Enter File %d name: ", j + 1); scanf("%s", dirs[i].fname[j]);
        }
    }
    printf("\nMaster Directory (MFD)\n");
    for (i = 0; i < d; i++) {
        printf("|-- %s (UFD)\n", dirs[i].dname);
        for (j = 0; j < dirs[i].fcnt; j++) printf("    |-- %s\n", dirs[i].fname[j]);
    }
}

void hierarchical() {
    int n, i, j, depth, p;
    struct { char name[20]; int is_dir; int parent; } t[20];
    
    printf("\nEnter root directory name: "); scanf("%s", t[0].name);
    t[0].is_dir = 1; t[0].parent = -1;
    
    printf("Enter number of sub-nodes (files/dirs): "); scanf("%d", &n);
    for (i = 1; i <= n; i++) {
        printf("Node %d name: ", i); scanf("%s", t[i].name);
        printf("Is it a Directory (1) or File (0)? "); scanf("%d", &t[i].is_dir);
        printf("Enter Parent Node Index (0 to %d): ", i - 1); scanf("%d", &t[i].parent);
    }
    
    printf("\nHierarchical Tree Structure:\n");
    for (i = 0; i <= n; i++) {
        depth = 0; p = t[i].parent;
        while (p != -1) { depth++; p = t[p].parent; }
        
        for (j = 0; j < depth; j++) printf("    ");
        if (i == 0) printf("%s (Root)\n", t[i].name);
        else printf("|-- %s %s\n", t[i].name, t[i].is_dir ? "(Dir)" : "(File)");
    }
}

int main() {
    int ch;
    while (1) {
        printf("\n--- File Organization Techniques ---\n");
        printf("1. Single Level  2. Two Level  3. Hierarchical  4. Exit\n");
        printf("Enter your choice: ");
        scanf("%d", &ch);
        
        switch (ch) {
            case 1: single_level(); break;
            case 2: two_level(); break;
            case 3: hierarchical(); break;
            case 4: return 0;
            default: printf("Invalid choice!\n");
        }
    }
    return 0;
}
/* Output:
--- File Organization Techniques ---
1. Single Level  2. Two Level  3. Hierarchical  4. Exit
Enter your choice: 2

Enter number of user directories: 2
Enter Dir 1 name: UserA
Number of files in UserA: 2
Enter File 1 name: doc1.txt
Enter File 2 name: img.png
Enter Dir 2 name: UserB
Number of files in UserB: 1
Enter File 1 name: data.csv

Master Directory (MFD)
|-- UserA (UFD)
    |-- doc1.txt
    |-- img.png
|-- UserB (UFD)
    |-- data.csv

--- File Organization Techniques ---
1. Single Level  2. Two Level  3. Hierarchical  4. Exit
Enter your choice: 3

Enter root directory name: root
Enter number of sub-nodes (files/dirs): 3
Node 1 name: home
Is it a Directory (1) or File (0)? 1
Enter Parent Node Index (0 to 0): 0
Node 2 name: os_lab.c
Is it a Directory (1) or File (0)? 0
Enter Parent Node Index (0 to 1): 1
Node 3 name: bin
Is it a Directory (1) or File (0)? 1
Enter Parent Node Index (0 to 2): 0

Hierarchical Tree Structure:
root (Root)
    |-- home (Dir)
        |-- os_lab.c (File)
    |-- bin (Dir)
*/
