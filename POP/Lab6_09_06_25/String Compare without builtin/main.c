#include <stdio.h>
#include <stdlib.h>

int main()
{
    char s1[20], s2[20];
    int i=0;
    printf("Enter string 1: ");
    gets(s1);
    printf("Enter string 2: ");
    gets(s2);
    while (s1[i]==s2[i]){i++;};
    if (s1[i]>s2[i]){printf("First String is greater. ");}
    else if (s1[i]<s2[i]){printf("Second String is greater. ");}
    else {printf("Both are equal.");}
    return 0;

}
