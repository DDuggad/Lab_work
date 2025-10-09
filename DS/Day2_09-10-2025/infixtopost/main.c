#include <stdio.h>
#include <stdlib.h>

int top1=-1, top2=-1, top3=-1 ;
char stack1[10], stack2[10], stack3[10];
void push (char a, int c){
    if (c==1){top1+=1; stack1[top1]=a;}
    else if (c==2){top2+=1; stack2[top2]=a;}
}

char pop (char a){ top2-=1; return a[top2+1];}
int main(){
    printf("Enter infix expression (length less than 9): ")
    gets(stack3);
    top3=0;


}
