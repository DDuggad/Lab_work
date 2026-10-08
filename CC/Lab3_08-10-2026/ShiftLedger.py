import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    n = int(data[0])
    
    total_mins = 0
    overnight = 0
    
    for i in range(n):
        sh, sm = map(int, data[1 + 2 * i].split(':'))
        eh, em = map(int, data[2 + 2 * i].split(':'))
        
        start = sh * 60 + sm
        end = eh * 60 + em
        
        if end <= start:
            end += 1440
            overnight += 1
            
        total_mins += end - start
        
    print(f"{total_mins} {overnight}")

if __name__ == "__main__":
    main()
