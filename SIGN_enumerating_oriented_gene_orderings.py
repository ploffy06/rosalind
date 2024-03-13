import itertools

n = 5
list_n = [-i for i in range(1, n+1)]
list_n.extend([i for i in range(1, n+1)])

perms = []
for perm in itertools.permutations(list_n, n):
    if len(set(abs(x) for x in perm)) == n:
        perms.append(perm)

print(len(perms))
for perm in perms:
    print(' '.join(str(p) for p in perm))