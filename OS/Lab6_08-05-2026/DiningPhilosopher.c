#include <stdio.h>
#include <pthread.h>
#include <semaphore.h>
#include <unistd.h>

sem_t forks[5];

void* philosopher(void* num) {
    int i = *(int*)num;

    printf("Philosopher %d is thinking\n", i);
    
    sem_wait(&forks[i]);           // Pick up left fork
    sem_wait(&forks[(i + 1) % 5]); // Pick up right fork

    printf("Philosopher %d is eating\n", i);
    sleep(1);

    printf("Philosopher %d finished eating\n", i);

    sem_post(&forks[i]);
    sem_post(&forks[(i + 1) % 5]);
}

int main() {
    int i, a[5];
    pthread_t tid[5];

    for (i = 0; i < 5; i++) sem_init(&forks[i], 0, 1);

    for (i = 0; i < 5; i++) {
        a[i] = i;
        pthread_create(&tid[i], NULL, philosopher, &a[i]);
    }

    for (i = 0; i < 5; i++) pthread_join(tid[i], NULL);

    return 0;
}
/* Output:
Philosopher 0 is thinking
Philosopher 0 is eating
Philosopher 1 is thinking
Philosopher 0 finished eating
Philosopher 1 is eating
...
*/