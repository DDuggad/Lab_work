#include <stdio.h>
int main()
{
    FILE *fp;
    char c;
    printf("Data read from the keyboard : \n");
    fp = fopen("BMSCE.txt", "a");
    while((c=getchar()) != EOF)
    fputc(c, fp);
    fclose(fp);
    printf("\nData Output\n\n");
    fp = fopen("BMSCE.txt", "r");
    while((c=fgetc(fp)) != EOF)
    printf("%c", c);
    fclose(fp);
    return 0;

}
