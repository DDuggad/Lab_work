#include <stdio.h>
#include <stdlib.h>

#define MAX_SIZE 5

int queue[MAX_SIZE];
int front = -1;
int rear = -1;

void insert() {
    if (rear == MAX_SIZE - 1) {
        printf("!! Queue Overflow !!\n");
        return;
    }
    if (front == -1) {
        front = 0;
    }
    printf("Enter the element to insert: ");
    rear++;
    scanf("%d", &queue[rear]);
    printf("%d inserted into the queue.\n", queue[rear]);
}

void delete() {
    if (front == -1 || front > rear) {
        printf("!! Queue Underflow !!\n");
        front = rear = -1;
        return;
    }
    printf("Element deleted from queue is: %d\n", queue[front]);
    front++;
}

void display() {
    if (front == -1) {
        printf("Queue is empty.\n");
        return;
    }
    printf("Queue elements are: ");
    for (int i = front; i <= rear; i++) {
        printf("%d ", queue[i]);
    }
    printf("\n");
}

int main() {
    int choice;
    while (1) {
        printf("\n1. Insert\n2. Delete\n3. Display\n4. Exit\nEnter your choice: ");
        scanf("%d", &choice);
        switch (choice) {
            case 1: insert(); break;
            case 2: delete(); break;
            case 3: display(); break;
            case 4: exit(0);
            default: printf("Invalid choice!\n");
        }
    }
    return 0;
}

