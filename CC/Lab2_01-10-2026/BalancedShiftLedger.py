import sys

def main():
    data = sys.stdin.read().split()
    s = data[0] if data else ""
    
    balance = 0
    first_seen = {0: -1} # Base case: balance 0 exists before the string starts
    
    max_len = 0
    best_start_idx = -1
    
    for i, char in enumerate(s):
        if char == 'C':
            balance += 1
        elif char == 'D':
            balance -= 1
            
        if balance in first_seen:
            current_len = i - first_seen[balance]
            
            # Use strictly greater (>) to ensure we keep the leftmost occurrence in case of a tie
            if current_len > max_len:
                max_len = current_len
                best_start_idx = first_seen[balance] + 1
        else:
            first_seen[balance] = i
            
    if max_len == 0:
        print("0 -1")
    else:
        print(f"{max_len} {best_start_idx}")

if __name__ == "__main__":
    main()
