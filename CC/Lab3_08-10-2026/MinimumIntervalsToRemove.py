import json
import sys

def erase_overlap_intervals(payload):
    intervals = payload.get("intervals", [])
    if not intervals:
        return 0
    intervals.sort(key=lambda x: x[1])
    kept = 0
    last_end = float('-inf')
    for start, end in intervals:
        if start >= last_end:
            kept += 1
            last_end = end
    return len(intervals) - kept

if __name__ == "__main__":
    payload = json.loads(sys.stdin.read() or "{}")
    print(json.dumps(erase_overlap_intervals(payload), separators=(",", ":")))
