# every tree has num_edges = num_nodes - 1

file = open('data.txt', 'r')
n = int(file.readline().replace('\n', ''))
pairs = [pair.replace('\n', '')  for pair in file.readlines()]
file.close()

num_edges = len(pairs)
e = n - 1

print(e - num_edges)