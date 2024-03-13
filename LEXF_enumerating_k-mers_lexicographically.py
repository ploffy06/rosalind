import itertools

file = open('data.txt', 'r')

symbols = file.readline().replace('\n', '').replace(' ', '')
n = file.readline().replace('\n', '')

file.close()

permutations = []
for perm in itertools.product(symbols, repeat=int(n)):
    permutations.append(perm)

for perm in permutations:
    for p in perm:
        print(p, end='')
    print()

