import sys
import json

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def build_tree(vals):
    if not vals or vals[0] is None:
        return None
    root = TreeNode(vals[0])
    q = [root]
    i = 1
    while q and i < len(vals):
        curr = q.pop(0)
        if i < len(vals) and vals[i] is not None:
            curr.left = TreeNode(vals[i])
            q.append(curr.left)
        i += 1
        if i < len(vals) and vals[i] is not None:
            curr.right = TreeNode(vals[i])
            q.append(curr.right)
        i += 1
    return root

def validate(node, low=float('-inf'), high=float('inf')):
    if not node:
        return True
    if not (low < node.val < high):
        return False
    return validate(node.left, low, node.val) and validate(node.right, node.val, high)

def solve():
    raw = sys.stdin.read().strip()
    if not raw or raw == "[]":
        print("true")
        return
    vals = json.loads(raw)
    root = build_tree(vals)
    print("true" if validate(root) else "false")

if __name__ == "__main__":
    solve()
