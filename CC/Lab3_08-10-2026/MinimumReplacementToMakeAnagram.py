import json
import sys
from collections import Counter

def min_anagram_replacements(payload):
    s = payload.get("s", "")
    t = payload.get("t", "")
    cs = Counter(s)
    ct = Counter(t)
    return sum(max(0, cs[c] - ct[c]) for c in cs)

if __name__ == "__main__":
    payload = json.loads(sys.stdin.read() or "{}")
    print(json.dumps(min_anagram_replacements(payload), separators=(",", ":")))
