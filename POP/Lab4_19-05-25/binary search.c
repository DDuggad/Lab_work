#include <stdio.h>
#include <stdlib.h>

int main()
{
    int n,i,mid,low,high,key;
    printf("Enter number of elements in array: ");
    scanf("%d", &n);
    int arr[n];
    printf("Enter the elements: \n");
    for (i=0;i<n;i++){
        scanf("%d",&arr[i]);
    }
    printf("Enter the element to be searched: ");
    scanf("%d",&key);
    low=0;
    high=n-1;
    while (low<=high){
        mid=(low+high)/2;
        if (key==arr[mid]){
            printf("The element to be searched is found at %d position. \n",mid+1);
            return(0);}
        else if (key<arr[mid]){
            high=high-1;
            }
        else {
            low=low+1;
            }
    }
    printf("Error!!");

}
