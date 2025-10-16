#include <stdio.h>
#include <stdlib.h>

int main()
{
    printf("Enter a string: ");
    char s1[10], s2[10];
    gets(s1);
    int i=0;
    while (s1[i]!='\0'){
        s2[i]=s1[i];
        i++;
    }
    s2[i]='\0';
    printf("The copied string is: %s",s2);
    return 0;

}
