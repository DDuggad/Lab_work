int main()
{
    int n,i;
    printf("Enter number of elements in array: ");
    scanf("%d", &n);
    int arr[n];
    printf("Enter the elements: \n");
    for (i=0;i<n;i++){
        scanf("%d",&arr[i]);
    }
    for (i=0;i<n;i++){
        printf(" %d ",arr[i]);
    }
    return 0;
}
