#include <stdio.h>
void swap_val(int, int);
void swap_ref(int *, int *);

int main()
{
    int choice,a,b;
    printf("\n Enter two numbers for a & b: ");
    scanf("%d %d",&a,&b);
    printf("\nEntered value are: a= %d & b=%d.\n",a,b);
    printf("\nEnter 1 for pass by value and 2 for pass by reference. \n");
    scanf("%d",&choice);
    if (choice==1){
        swap_val(a,b);
    }
    else if (choice==2){
        swap_ref(&a,&b);
        printf("\nNew Values: a= %d & b=%d. ",a,b);
    }
    return 0;
}

void swap_val( int m, int n){
m=n+m;
n=m-n;
m=m-n;
printf("\nNew Values: a= %d & b=%d. ",m,n);
}

void swap_ref(int *m, int *n){
*m=*n+*m;
*n=*m-*n;
*m=*m-*n;
}
