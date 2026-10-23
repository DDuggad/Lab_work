import sys
from collections import deque

def main():
    lines = sys.stdin.read().splitlines()
    if not lines:
        return
    q = int(lines[0])

    q_tokens = deque()
    patient = {}
    status = {}
    next_token = 1
    waiting_count = 0
    out = []

    for i in range(1, 1 + q):
        parts = lines[i].split()
        op = parts[0]
        if op == "ARRIVE":
            name = parts[1]
            t = next_token
            next_token += 1
            patient[t] = name
            status[t] = 0
            q_tokens.append(t)
            waiting_count += 1
            out.append(str(t))
        elif op == "CANCEL":
            t = int(parts[1])
            if status.get(t) == 0:
                status[t] = 2
                waiting_count -= 1
                out.append("OK")
            else:
                out.append("NOT_WAITING")
        elif op == "CALL":
            while q_tokens and status[q_tokens[0]] != 0:
                q_tokens.popleft()
            if not q_tokens:
                out.append("EMPTY")
            else:
                t = q_tokens.popleft()
                status[t] = 1
                waiting_count -= 1
                out.append(f"{t} {patient[t]}")
        elif op == "WAITING":
            out.append(str(waiting_count))

    print("\n".join(out))

if __name__ == "__main__":
    main()
