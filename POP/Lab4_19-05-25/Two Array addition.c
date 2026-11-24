int main()
{
    int n,i;
    printf("Enter number of elements in array: ");
    scanf("%d", &n);
    int arr1[n],arr2[n],res[n];
    printf("Enter the elements of Array 1: \n");
    for (i=0;i<n;i++){
        scanf("%d",&arr1[i]);
    }
    printf("\nEnter the elements of Array 2: \n");
    for (i=0;i<n;i++){
        scanf("%d",&arr2[i]);
    }
    for (i=0;i<n;i++){
        res[i]=arr1[i]+arr2[i];
    }
    printf("\nThe Resultant array is : \n");
    for (i=0;i<n;i++){
        printf("%d ",res[i]);
    }
    return 0;
}
