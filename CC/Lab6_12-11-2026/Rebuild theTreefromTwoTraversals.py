import sys

sys.setrecursionlimit(20000)

def main():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    n = int(data[0])
    pre = [int(x) for x in data[1:1 + n]]
    ino = [int(x) for x in data[1 + n:1 + 2 * n]]

    in_map = {val: idx for idx, val in enumerate(ino)}
    post = []

    def build(p_start, p_end, i_start, i_end):
        if p_start > p_end:
            return
        root = pre[p_start]
        i_root = in_map[root]
        left_size = i_root - i_start

        build(p_start + 1, p_start + left_size, i_start, i_root - 1)
        build(p_start + left_size + 1, p_end, i_root + 1, i_end)
        post.append(str(root))

    build(0, n - 1, 0, n - 1)
    print(" ".join(post))

if __name__ == "__main__":
    main()
