#include <stdio.h>
#include <stdlib.h>

int main()
{
    int m,n,i,j;
    printf("Enter number of rows and columns: ");
    scanf("%d %d",&m,&n);
    int arr1[m][n],arr2[n][m];

    printf("Enter the Matrix.\n");
    for (i=0;i<m;i++){
        for (j=0;j<n;j++){
            printf("Enter %dx%d element: ",i+1,j+1);
            scanf("%d",&arr1[i][j]);
        }
    }

    for (i=0;i<m;i++){
        for (j=0;j<n;j++){
            arr2[j][i]=arr1[i][j];
        }
    }
    printf("\nThe Transposed Matrix is: \n");
    for (i=0;i<m;i++){
        for (j=0;j<n;j++){
            printf("%d ",arr2[i][j]);
        }
        printf("\n");
    }

    return 0;
}
