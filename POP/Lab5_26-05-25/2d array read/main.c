#include <stdio.h>
#include <stdlib.h>

int main()
{
    int m,n,i,j;
    printf("Enter number of rows and columns: ");
    scanf("%d %d",&m,&n);
    int arr[m][n];
    for (i=0;i<m;i++){
        for (j=0;j<n;j++){
            printf("Enter %dx%d element: ",i+1,j+1);
            scanf("%d",&arr[i][j]);
        }
    }
    printf("\nThe entered 2D array is: \n");
    for (i=0;i<m;i++){
        for (j=0;j<n;j++){
            printf("%d ",arr[i][j]);
        }
        printf("\n");
    }

    return 0;
}
