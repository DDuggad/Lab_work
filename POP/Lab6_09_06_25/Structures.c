#include <stdio.h>
#include <stdlib.h>

struct date_of_birth
{
    int dd;
    int mm;
    int yy;
};

struct employee
{
    int eno;
    char ename[20];
    struct date_of_birth DOB;
    int salary;
} emp[10];

int main()
{
    int i, n, sal_sum = 0, sal_avg = 0;

    printf("How many employee records do you want to enter? ");
    scanf("%d", &n);

    if (n > 10)
    {
        printf("You can enter up to 10 employees only.\n");
        return 1;
    }

    printf("Enter details for %d employees:\n", n);

    for (i = 0; i < n; i++)
    {
        printf("\nEmployee %d\n", i + 1);

        printf("Employee number: ");
        scanf("%d", &emp[i].eno);

        printf("Name: ");
        scanf("%s", emp[i].ename);

        printf("Enter Date of Birth [DD MM YYYY]: ");
        scanf("%d %d %d", &emp[i].DOB.dd, &emp[i].DOB.mm, &emp[i].DOB.yy);

        printf("Enter Salary: ");
        scanf("%d", &emp[i].salary);
    }

    for (i = 0; i < n; i++)
    {
        sal_sum += emp[i].salary;
    }

    sal_avg = (n > 0) ? sal_sum / n : 0;
    printf("\nThe average salary of the employees is %d\n", sal_avg);

    return 0;
}
