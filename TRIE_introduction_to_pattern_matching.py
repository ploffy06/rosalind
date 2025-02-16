class Trie:
    def __init__(self, value=None, node=1):
        self.value = value
        self.node = node
        self.children = []

    def get_child(self, value):
        for child in self.children:
            if child.value == value:
                return child
        return None

    def add_child(self, valud, node):
        new_child = Trie(valud, node)
        self.children.append(new_child)

        return new_child

file = open('data.txt', 'r')
lines = file.readlines()
file.close()
dna_strings = [l.replace('\n', '') for l in lines]

total_nodes = 0

# create first node
total_nodes += 1
head = Trie(value=None, node=total_nodes)

for dna in dna_strings:
    curr = head
    for base in dna:
        new = curr.get_child(base)
        if new == None:
            total_nodes += 1
            new = curr.add_child(base, total_nodes)
            print(curr.node, total_nodes, base)
        curr = new
