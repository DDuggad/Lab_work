#include <stdbool.h>
#include <stdlib.h>

bool canFinish(int numCourses, int** prerequisites, int prerequisitesSize, int* prerequisitesColSize) {
    int* inDegree = (int*)calloc(numCourses, sizeof(int));
    int* queue = (int*)malloc(numCourses * sizeof(int));    
    int front = 0, rear = 0, count = 0;
    for (int i = 0; i < prerequisitesSize; i++) {
        int course = prerequisites[i][0];
        inDegree[course]++;
    }
    for (int i = 0; i < numCourses; i++) {
        if (inDegree[i] == 0) {
            queue[rear++] = i;
        }
    }
    while (front < rear) {
        int u = queue[front++]; 
        count++;
        for (int i = 0; i < prerequisitesSize; i++) {
            int prereq = prerequisites[i][1];
            int course = prerequisites[i][0];
            
            if (prereq == u) {
                inDegree[course]--;
                if (inDegree[course] == 0) {
                    queue[rear++] = course;
                }
            }
        }
    }
    free(inDegree);
    free(queue);
    return count == numCourses;
}
