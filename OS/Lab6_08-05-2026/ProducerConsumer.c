#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <semaphore.h>

#define SIZE 5

int buffer[SIZE], in = 0, out = 0;
sem_t mutex, empty, full;

void* producer(void* arg) {
    int item = rand() % 100;
    sem_wait(&empty);
    sem_wait(&mutex);
    
    buffer[in] = item;
    printf("Producer produced: %d\n", item);
    in = (in + 1) % SIZE;
    
    sem_post(&mutex);
    sem_post(&full);
}

void* consumer(void* arg) {
    sem_wait(&full);
    sem_wait(&mutex);
    
    int item = buffer[out];
    printf("Consumer consumed: %d\n", item);
    out = (out + 1) % SIZE;
    
    sem_post(&mutex);
    sem_post(&empty);
}

int main() {
    pthread_t p[5], c[5];
    sem_init(&mutex, 0, 1);
    sem_init(&empty, 0, SIZE);
    sem_init(&full, 0, 0);

    for(int i = 0; i < 5; i++) {
        pthread_create(&p[i], NULL, producer, NULL);
        pthread_create(&c[i], NULL, consumer, NULL);
    }

    for(int i = 0; i < 5; i++) {
        pthread_join(p[i], NULL);
        pthread_join(c[i], NULL);
    }

    sem_destroy(&mutex);
    sem_destroy(&empty);
    sem_destroy(&full);
    return 0;
}
/* Output:
Producer produced: 83
Consumer consumed: 83
Producer produced: 86
Consumer consumed: 86
Producer produced: 77
Consumer consumed: 77
...
*/