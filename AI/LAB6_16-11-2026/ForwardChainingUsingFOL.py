def parse(atom):
    atom = atom.strip()
    if '(' not in atom:
        return (atom, [])
    name, rest = atom.split('(', 1)
    args = [x.strip() for x in rest[:-1].split(',')]
    return (name.strip(), args)

def fmt(atom):
    return f"{atom[0]}({','.join(atom[1])})" if atom[1] else atom[0]

def subst(atom, theta):
    return (atom[0], [theta.get(a, a) for a in atom[1]])

def unify(a, b, theta):
    if a[0] != b[0] or len(a[1]) != len(b[1]):
        return None
    t = dict(theta)
    for x, y in zip(a[1], b[1]):
        x, y = t.get(x, x), t.get(y, y)
        if x == y:
            continue
        if x[0].islower():
            t[x] = y
        elif y[0].islower():
            t[y] = x
        else:
            return None
    return t

def match(prems, facts, theta):
    if not prems:
        return [theta]
    res = []
    first = subst(prems[0], theta)
    for f in facts:
        nt = unify(first, f, theta)
        if nt is not None:
            res.extend(match(prems[1:], facts, nt))
    return res

rules = []
r_count = int(input("Enter number of rules: "))
for _ in range(r_count):
    lhs, rhs = input("Rule (e.g. P(x) & Q(x) -> R(x)): ").split('->')
    rules.append(([parse(p) for p in lhs.split('&')], parse(rhs)))

facts = []
f_count = int(input("Enter number of facts: "))
for _ in range(f_count):
    facts.append(parse(input("Fact: ")))

query = parse(input("Enter query: "))

proven = query in facts
while not proven:
    added = False
    for prems, conc in rules:
        for theta in match(prems, facts, {}):
            nf = subst(conc, theta)
            if nf not in facts:
                facts.append(nf)
                print("Derived:", fmt(nf))
                added = True
                if nf == query:
                    proven = True
                    break
        if proven:
            break
    if not added:
        break

print("Result:", "Query Proven" if proven else "Cannot Prove Query")
