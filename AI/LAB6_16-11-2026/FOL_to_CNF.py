import re

def parse(s):
    tokens = re.findall(r'<->|->|[~&|(),]|[A-Za-z0-9_]+', s)
    pos = [0]

    def peek():
        return tokens[pos[0]] if pos[0] < len(tokens) else None

    def consume():
        t = tokens[pos[0]]
        pos[0] += 1
        return t

    def iff():
        a = imp()
        while peek() == '<->':
            consume()
            a = ('iff', a, imp())
        return a

    def imp():
        a = or_expr()
        if peek() == '->':
            consume()
            a = ('imp', a, imp())
        return a

    def or_expr():
        a = and_expr()
        while peek() == '|':
            consume()
            a = ('or', a, and_expr())
        return a

    def and_expr():
        a = atom()
        while peek() == '&':
            consume()
            a = ('and', a, atom())
        return a

    def atom():
        t = peek()
        if t == '~':
            consume()
            return ('not', atom())
        if t in ('forall', 'exists'):
            q = consume()
            v = consume()
            return (q, v, atom())
        if t == '(':
            consume()
            a = iff()
            consume()
            return a
        name = consume()
        args = []
        if peek() == '(':
            consume()
            while peek() != ')':
                if peek() == ',':
                    consume()
                else:
                    args.append(consume())
            consume()
        return ('pred', name, args)

    return iff()

def elim_imp(n):
    op = n[0]
    if op == 'iff':
        return elim_imp(('and', ('imp', n[1], n[2]), ('imp', n[2], n[1])))
    if op == 'imp':
        return ('or', ('not', elim_imp(n[1])), elim_imp(n[2]))
    if op in ('and', 'or'):
        return (op, elim_imp(n[1]), elim_imp(n[2]))
    if op == 'not':
        return ('not', elim_imp(n[1]))
    if op in ('forall', 'exists'):
        return (op, n[1], elim_imp(n[2]))
    return n

def move_not(n):
    op = n[0]
    if op == 'not':
        c = n[1]
        if c[0] == 'not':
            return move_not(c[1])
        if c[0] == 'and':
            return ('or', move_not(('not', c[1])), move_not(('not', c[2])))
        if c[0] == 'or':
            return ('and', move_not(('not', c[1])), move_not(('not', c[2])))
        if c[0] == 'forall':
            return ('exists', c[1], move_not(('not', c[2])))
        if c[0] == 'exists':
            return ('forall', c[1], move_not(('not', c[2])))
        return ('not', move_not(c))
    if op in ('and', 'or'):
        return (op, move_not(n[1]), move_not(n[2]))
    if op in ('forall', 'exists'):
        return (op, n[1], move_not(n[2]))
    return n

def skolemize(n, uvars, subs, cnt, used):
    op = n[0]
    if op == 'forall':
        v = n[1]
        nv = v if v not in used else f"{v}{len(used)}"
        used.add(nv)
        ns = dict(subs, **{v: nv})
        return skolemize(n[2], uvars + [nv], ns, cnt, used)
    if op == 'exists':
        v = n[1]
        cnt[0] += 1
        sk = f"F{cnt[0]}({','.join(uvars)})" if uvars else f"C{cnt[0]}"
        ns = dict(subs, **{v: sk})
        return skolemize(n[2], uvars, ns, cnt, used)
    if op in ('and', 'or'):
        return (op, skolemize(n[1], uvars, subs, cnt, used), skolemize(n[2], uvars, subs, cnt, used))
    if op == 'not':
        return ('not', skolemize(n[1], uvars, subs, cnt, used))
    args = [subs.get(a, a) for a in n[2]]
    return ('pred', n[1], args)

def dist(n):
    op = n[0]
    if op == 'and':
        return ('and', dist(n[1]), dist(n[2]))
    if op == 'or':
        a, b = dist(n[1]), dist(n[2])
        if a[0] == 'and':
            return ('and', dist(('or', a[1], b)), dist(('or', a[2], b)))
        if b[0] == 'and':
            return ('and', dist(('or', a, b[1])), dist(('or', a, b[2])))
        return ('or', a, b)
    return n

def fmt(n):
    op = n[0]
    if op == 'pred':
        return f"{n[1]}({','.join(n[2])})" if n[2] else n[1]
    if op == 'not':
        return f"~{fmt(n[1])}"
    if op == 'and':
        return f"({fmt(n[1])} & {fmt(n[2])})"
    if op == 'or':
        return f"({fmt(n[1])} | {fmt(n[2])})"

expr = input("Enter FOL statement: ")
tree = parse(expr)
tree = elim_imp(tree)
tree = move_not(tree)
tree = skolemize(tree, [], {}, [0], set())
tree = dist(tree)
print("CNF:", fmt(tree))
