#include <stdio.h>
#include <stdlib.h>

int main(){
    int n,i,m,a=0;
    printf("Enter no. of elements in array: ");
    scanf("%d",&n);
    int arr[n];
    arr[0]=0;
    for (i=0;i<n;i++){
        printf("Enter the position for element to inserted: ");
        scanf("%d",&m);
        printf("Enter the element: ");
        if (arr[m-1]==0){scanf("%d",&arr[m-1]);}
        else {for(a=n-1;a>=m;a--){
            arr[a]=arr[a-1];}
            scanf("%d",&arr[m-1]);
        }
    }
    printf("The newly updated array is: \n");
    for (i=0;i<n;i++){
        printf("%d\t",arr[i]);
    }
    return 0;
}
