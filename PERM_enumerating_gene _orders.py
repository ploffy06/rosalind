import itertools # sorry kind of hacky

n = 7

permutations = []
nums = [i for i in range(1, n+1)]
for perm in itertools.permutations(nums):
    permutations.append(perm)

print(len(permutations))
for perm in permutations:
    print(' '.join(map(str, perm)))