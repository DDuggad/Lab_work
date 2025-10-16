int main()
{
    int n,i,sum=0;
    printf("Enter number of elements in array: ");
    scanf("%d", &n);
    int arr[n];
    printf("Enter the elements: \n");
    for (i=0;i<n;i++){
        scanf("%d",&arr[i]);
    }
    for (i=0;i<n;i++){
        sum+=arr[i];
    }
    printf("\nThe sum of array elements is : %d .",sum);
    return 0;
}
