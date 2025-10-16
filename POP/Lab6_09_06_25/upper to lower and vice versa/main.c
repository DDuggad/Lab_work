#include <stdio.h>
#include <stdlib.h>

int main()
{
    char string[10];
    printf("Enter a string: ");
    scanf("%s",string);
    char lower [10],upper[10];
    int i=0;
    while (string[i]!='\0'){
        if (string[i]>='a' && string[i]<='z'){
            lower[i]=string[i];
            upper[i]=string[i]-32;
        }
        else if (string[i]>='A' && string[i]<='Z'){
            upper[i]=string[i];
            lower[i]=string[i]+32;
        }
        i++;
    }
    upper[i]='\0';
    lower[i]='\0';
    printf("\nThe entered string is: %s\nUpper Case: %s\nLower Case: %s",string,upper,lower);
    return 0;
}
