#include <stdio.h>
#include <stdlib.h>

int main()
{
    printf("Enter a string: ");
    char s1[10], s2[10];
    gets(s1);
    strcpy(s2,s1);
    printf("The copied string is: %s",s2);
    return 0;

}
