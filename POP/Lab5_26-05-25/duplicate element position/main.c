#include <stdio.h>
#include <stdlib.h>

int main()
{
    int n,i,pos,count=0;
    printf("Enter number of elements in array: ");
    scanf("%d",&n);
    int arr[n],dup[n];
    dup[0]=0;
    for (i=0;i<n;i++){
        printf("Enter %d element of array: ",i+1);
        scanf("%d",&arr[i]);
    }
    for (i=0;i<n;i++){
        if (dup[i]==1){continue;}
        count=0;
        printf("\nThe element %d is repeated at position: ",arr[i]);
        for (pos=i+1;pos<n;pos++){
            if (arr[i]==arr[pos]){
                printf("%d ",pos+1);
                count+=1;
                dup[pos]=1;
            }
        }
        if (count==0){printf("Nowhere, unique element.");}
    }
}
