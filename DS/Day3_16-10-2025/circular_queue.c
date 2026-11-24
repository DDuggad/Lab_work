#include <stdio.h>
#include <stdlib.h>

#define MAX_SIZE 5

int c_queue[MAX_SIZE];
int front = -1;
int rear = -1;

void c_insert() {
    if ((rear + 1) % MAX_SIZE == front) {
        printf("!! Queue Overflow !!\n");
        return;
    }
    if (front == -1) {
        front = 0;
    }
    printf("Enter the element to insert: ");
    rear = (rear + 1) % MAX_SIZE;
    scanf("%d", &c_queue[rear]);
    printf("%d inserted into the queue.\n", c_queue[rear]);
}

void c_delete() {
    if (front == -1) {
        printf("!! Queue Underflow !!\n");
        return;
    }
    printf("Element deleted from queue is: %d\n", c_queue[front]);
    if (front == rear) {
        front = -1;
        rear = -1;
    } else {
        front = (front + 1) % MAX_SIZE;
    }
}

void c_display() {
    if (front == -1) {
        printf("Queue is empty.\n");
        return;
    }
    printf("Queue elements are: ");
    int i;
    for (i = front; i != rear; i = (i + 1) % MAX_SIZE) {
        printf("%d ", c_queue[i]);
    }
    printf("%d\n", c_queue[i]);
}

int main() {
    int choice;
    while (1) {
        printf("\n1. Insert\n2. Delete\n3. Display\n4. Exit\nEnter your choice: ");
        scanf("%d", &choice);
        switch (choice) {
            case 1: c_insert(); break;
            case 2: c_delete(); break;
            case 3: c_display(); break;
            case 4: exit(0);
            default: printf("Invalid choice!\n");
        }
    }
    return 0;
}

