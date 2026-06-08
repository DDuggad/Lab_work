#include <stdlib.h>
#include <math.h>

int board[10], res_count;
char*** result;

int place(int row, int col) {
    for (int i = 0; i < row; i++) {
        if (board[i] == col || abs(board[i] - col) == abs(i - row)) return 0;
    }
    return 1;
}

void nQueens(int row, int n) {
    if (row == n) {
        char** sol = (char**)malloc(n * sizeof(char*));
        for (int i = 0; i < n; i++) {
            sol[i] = (char*)malloc((n + 1) * sizeof(char));
            for (int j = 0; j < n; j++) {
                sol[i][j] = (board[i] == j) ? 'Q' : '.';
            }
            sol[i][n] = '\0';
        }
        result[res_count++] = sol;
        return;
    }
    for (int col = 0; col < n; col++) {
        if (place(row, col)) {
            board[row] = col;
            nQueens(row + 1, n);
        }
    }
}

char*** solveNQueens(int n, int* returnSize, int** returnColumnSizes) {
    result = (char***)malloc(400 * sizeof(char**)); 
    res_count = 0;
    
    nQueens(0, n);
    
    *returnSize = res_count;
    *returnColumnSizes = (int*)malloc(res_count * sizeof(int));
    for (int i = 0; i < res_count; i++) {
        (*returnColumnSizes)[i] = n;
    }
    
    return result;
}
