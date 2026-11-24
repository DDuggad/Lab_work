#include <stdio.h>
#include <string.h>
void lalli() {
    printf("Hello Lalli Bhai\n");
    printf("\nYour USN is 1WN24CS144\n");
}
void chira(m) {
    printf("Hello Ceenu Bhai\n");
    printf("\nYour USN is 1BF24CS091.\n");
    printf("The marks is %d", m);
}
int main() {
    char naam[20];
    int marks;
    printf("Enter name: ");
    scanf("%s", naam);
    printf("Enter marks: ");
    scanf("%d", &marks);
    if (strcmp(naam, "Lalli") == 0 || strcmp(naam, "Lalit") == 0 ||
        strcmp(naam, "Gillu") == 0 || strcmp(naam, "lalli") == 0 ||
        strcmp(naam, "lalit") == 0 || strcmp(naam, "gillu") == 0) {lalli();}
    else if (strcmp(naam, "Chirag") == 0 || strcmp(naam, "Ceenu") == 0 ||
               strcmp(naam, "chirag") == 0 || strcmp(naam, "ceenu") == 0 ||
               strcmp(naam, "Mukhija") == 0 || strcmp(naam, "mukhija") == 0) {chira(marks);}
    return 0;
}
