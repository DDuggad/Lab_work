#include <stdio.h>
struct employee
{
    int eno;
    char ename[20];
    struct dateOfBirth
    {
        int dd;
        int mm;
        int yy;
    }DOB;
    int salary;
}emp[10];
int main()
{
    int i, high, n, sal_sum = 0, sal_avg = 0;
    printf("How many employee info you want to accept: ");
    scanf("%d", &n);
    for (i = 0; i < n; i++)
    {
        printf("Enter Details for %d employee. \n",i+1);
        printf("Employee Number: ");
        scanf("%d", &emp[i].eno);
        printf("Name : ");
        scanf("%s", emp[i].ename);
        printf("Enter Date of Birth [DD MM YYYY] format: ");
        scanf("%d%d%d", &emp[i].DOB.dd,&emp[i].DOB.mm,&emp[i].DOB.yy);
        printf("Salary : ");
        scanf("%d", &emp[i].salary);
        printf("\n");
    }
    for (i = 0; i < n; i++)
    {
        sal_sum = sal_sum + emp[i].salary;
    }
    sal_avg = sal_sum / n;
    printf("The average salary of the employees is %d .\n", sal_avg);
    return 0;
}
