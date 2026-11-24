#include <stdio.h>
#include <stdlib.h>

int main()
{
    int i,M,N,sum=0;
    printf("Enter values of M & N: ");
    scanf("%d %d",&M,&N);
    printf("The list of even number between %d and %d is : ",M,N);
    for (i=M; i<=N;i++){
        if (i%2==0){
            printf("%d ",i);
            sum=sum+i;
        }
    }
    printf("The sum of even number is %d ",sum);
    return 0;

}
