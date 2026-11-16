import json
import sys
from collections import deque

def can_finish_courses(payload):
    n = payload.get("n", 0)
    prerequisites = payload.get("prerequisites", [])

    adj = [[] for _ in range(n)]
    in_degree = [0] * n

    for course, prereq in prerequisites:
        adj[prereq].append(course)
        in_degree[course] += 1

    queue = deque(i for i in range(n) if in_degree[i] == 0)
    completed = 0

    while queue:
        curr = queue.popleft()
        completed += 1
        for nxt in adj[curr]:
            in_degree[nxt] -= 1
            if in_degree[nxt] == 0:
                queue.append(nxt)

    return completed == n

if __name__ == "__main__":
    payload = json.loads(sys.stdin.read() or "{}")
    print(json.dumps(can_finish_courses(payload), separators=(",", ":")))
