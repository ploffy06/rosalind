import itertools

file = open('data.txt', 'r')
A = file.readline().replace('\n', '').replace(' ', '')
n = int(file.readline().replace('\n', ''))

perm_list = []

for i in range(1, n+1):
    for perm in itertools.product(A, repeat=int(i)):
        perm_str = ''.join(perm)
        perm_list.append(perm_str)

order = {symbol: i for i, symbol in enumerate(A)}
perm_list.sort(key=lambda x: tuple(order[symbol] for symbol in x))

print('\n'.join(map(str, perm_list)))

