from helper import getDNAStringsList, getRosalindLabels

dna_strings = getDNAStringsList()
labels = getRosalindLabels()
assert len(dna_strings) == len(labels)

dna_to_labels = { d:l for d, l in zip(dna_strings, labels)}


k = 3
overlap_graph = []

for s1 in dna_strings:
    for s2 in dna_strings:
        if s1 == s2:
            continue
        if s1[-3:] == s2[:3]:
            overlap_graph.append(f'{dna_to_labels[s1]} {dna_to_labels[s2]}')

for pair in overlap_graph:
    print(pair)