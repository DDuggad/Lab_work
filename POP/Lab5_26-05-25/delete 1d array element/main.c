#include <stdio.h>
#include <stdlib.h>

int main(){
    int n,i,pos;
    printf("Enter no. of elements in array: ");
    scanf("%d",&n);
    int arr[n];
    arr[0]=0;
    for (i=0;i<n;i++){
        printf("Enter the element for %d position: ",i+1);
        scanf("%d",&arr[i]);
        }

    printf("\nThe entered array is: \n");
    for (i=0;i<n;i++){
        printf("%d\t",arr[i]);
    }

    printf("\nEnter the position you want to delete: \n");
    scanf("%d",&pos);
    for (i=pos-1;i<n;i++){
        arr[i]=arr[i+1];
    }
    n--;

    printf("\nThe newly updated array is: \n");
    for (i=0;i<n;i++){
        printf("%d\t",arr[i]);
    }
    return 0;
}
